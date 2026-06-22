import json

def convert_date_format(date_str):
    try:
        year, month, day = date_str.split('-')
        return f"{day}/{month}/{year}"
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def process_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and len(value.split('-')) == 3:
                data[key] = convert_date_format(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, str) and len(item.split('-')) == 3:
                data[i] = convert_date_format(item)
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_json = {
        "event": "Conference",
        "date": "2023-12-31"
    }
    with open('sample.json', 'w') as file:
        json.dump(sample_json, file)
    
    process_json_file('sample.json')
    
    with open('sample.json', 'r') as file:
        updated_data = json.load(file)
        print(updated_data)