from google.cloud import storage
import json
import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.cityofchicago.org", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofchicago.org",
                "uxnrv7ZjS2c3jlrgMaXw9cNko",
                username="abeburton@me.com",
                password="js9@5x#H9@wp2#Y")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("m6dm-c72p")

# Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(results)

# Initialize a client
storage_client = storage.Client()

# Define your Google Cloud Storage bucket and file path
file_path = '/bdp-rideshare-project/rideshare.json'

# Convert the JSON object to a JSON string
json_data = json.dumps(results)

# Write the JSON data to Cloud Storage
with storage_client.bucket("msca-bdp-student-gcs").blob(file_path).open("w") as file:
    file.write(json_data)

print("JSON data written to Cloud Storage")
