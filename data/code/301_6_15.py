import json

def convert_date_format(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == 'date':
                json_data[key] = value.split('-')[2] + '/' + value.split('-')[1] + '/' + value.split('-')[0]
            else:
                convert_date_format(value)
    elif isinstance(json_data, list):
        for item in json_data:
            convert_date_format(item)

def main():
    sample_json = '''
    {
        "event": {
            "name": "Conference",
            "date": "2023-10-05"
        },
        "attendees": [
            {"name": "Alice", "date": "2023-10-06"},
            {"name": "Bob", "date": "2023-10-07"}
        ]
    }
    '''
    data = json.loads(sample_json)
    convert_date_format(data)
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    main()