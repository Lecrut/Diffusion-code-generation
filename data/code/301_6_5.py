import json

def convert_dates_in_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    def date_converter(date_str):
        year, month, day = date_str.split('-')
        return f'{day}/{month}/{year}'
    
    def recursive_date_conversion(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str) and len(value) == 10 and value.count('-') == 2:
                    obj[key] = date_converter(value)
                else:
                    recursive_date_conversion(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_date_conversion(item)
    
    recursive_date_conversion(data)
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_json = {
        "event": {
            "date": "2023-10-05",
            "participants": [
                {"name": "Alice", "dob": "1990-06-15"},
                {"name": "Bob", "dob": "1985-11-20"}
            ]
        }
    }
    
    with open('sample.json', 'w') as file:
        json.dump(sample_json, file, indent=4)
    
    convert_dates_in_json('sample.json')
    
    with open('sample.json', 'r') as file:
        updated_data = json.load(file)
        print(updated_data)