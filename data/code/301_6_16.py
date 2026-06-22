import json

def convert_date_format(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, str) and len(value) == 10 and value.count('-') == 2:
                try:
                    year, month, day = map(int, value.split('-'))
                    json_data[key] = f"{day:02d}/{month:02d}/{year}"
                except ValueError:
                    continue
            else:
                convert_date_format(value)
    elif isinstance(json_data, list):
        for item in json_data:
            convert_date_format(item)

if __name__ == '__main__':
    sample_json = {
        "event": "Conference",
        "date": "2023-12-31",
        "participants": [
            {"name": "Alice", "birthday": "1990-05-15"},
            {"name": "Bob", "birthday": "1985-01-01"}
        ]
    }
    convert_date_format(sample_json)
    print(json.dumps(sample_json, indent=2))