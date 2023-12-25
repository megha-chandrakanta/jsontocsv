import json
import pandas as pd

with open("C:\\Users\\Mgha\\Documents\\Py Projects\\test.json") as f:
    data = json.load(f)
    data = pd.json_normalize(data)
data.to_csv("C:\\Users\\Mgha\\Documents\\Py Projects\\test.csv", index=False)
print("Successfully converted")