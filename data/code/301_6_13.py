import json

def convert_date_format(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = convert_date_format(value)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            json_data[i] = convert_date_format(item)
    elif isinstance(json_data, str) and len(json_data) == 10 and json_data.replace('-', '').isdigit():
        return json_data[8:10] + '/' + json_data[5:7] + '/' + json_data[:4]
    return json_data

def process_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    converted_data = convert_date_format(data)
    
    with open(file_path, 'w') as file:
        json.dump(converted_data, file, indent=4)

if __name__ == '__main__':
    sample_json = '''
    {
        "event": "Conference",
        "date": "2023-10-05",
        "participants": [
            {"name": "Alice", "birthday": "1990-06-15"},
            {"name": "Bob", "birthday": "1985-11-20"}
        ]
    }
    '''
    
    sample_file_path = 'sample.json'
    with open(sample_file_path, 'w') as file:
        file.write(sample_json)
    
    process_json_file(sample_file_path)
    
    with open(sample_file_path, 'r') as file:
        print(json.load(file))