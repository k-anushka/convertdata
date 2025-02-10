import csv
import json

csv_file = open('test_data.csv', 'r')

csv_reader = csv.reader(csv_file)
field_names = next(csv_reader)
print(field_names)

data =[]

for row in csv_reader:
    cleaned_row = {field: (value if value.strip() else "None") for field, value in zip(field_names, row)}
    
    data.append(cleaned_row)
print(data)

json_data = json.dumps(data, indent=4)
json_file = open('data.json','w')
json_file .write(json_data)

csv_file.close()
json_file.close()