import json

def convert_date_format(json_data):
    def date_converter(date_str):
        return date_str.split('-')[2] + '/' + date_str.split('-')[1] + '/' + date_str.split('-')[0]

    if isinstance(json_data, dict):
        for key, value in json_data.items():
            json_data[key] = convert_date_format(value)
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            json_data[i] = convert_date_format(item)
    elif isinstance(json_data, str) and len(json_data.split('-')) == 3:
        return date_converter(json_data)

    return json_data

if __name__ == '__main__':
    sample_json = {
        "event": {
            "date": "2023-10-05",
            "details": {
                "start_date": "2023-09-20"
            }
        },
        "tasks": [
            {"due_date": "2023-11-15"},
            {"due_date": "2023-12-01"}
        ]
    }

    converted_json = convert_date_format(sample_json)
    print(json.dumps(converted_json, indent=4))