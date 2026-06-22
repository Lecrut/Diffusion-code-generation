import json

def convert_date_format(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = convert_date_format(value)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            json_data[i] = convert_date_format(item)
    elif isinstance(json_data, str) and len(json_data) == 10 and json_data[4] == '-' and json_data[7] == '-':
        year, month, day = json_data.split('-')
        return f'{day}/{month}/{year}'
    return json_data

if __name__ == '__main__':
    sample_json = '''
    {
        "event": "Conference",
        "date": "2023-10-05",
        "attendees": [
            {"name": "Alice", "dob": "1985-06-15"},
            {"name": "Bob", "dob": "1990-11-20"}
        ]
    }
    '''
    sample_json = json.loads(sample_json)
    converted_json = convert_date_format(sample_json)
    print(json.dumps(converted_json, indent=4))