import json

def convert_date_format(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = convert_date_format(value)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            json_data[i] = convert_date_format(item)
    elif isinstance(json_data, str) and len(json_data) == 10 and json_data.replace('-', '').isdigit():
        return '/'.join(reversed(json_data.split('-')))
    return json_data

if __name__ == '__main__':
    sample_json = '{"date": "2023-04-30", "events": [{"start_date": "2023-05-01"}, {"end_date": "2023-05-31"}]}'
    converted_json = convert_date_format(json.loads(sample_json))
    print(json.dumps(converted_json, indent=2))