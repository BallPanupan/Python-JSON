import json

# read file
with open('data.json') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
json_format = json.dumps(obj, indent=2)
print(json_format)
