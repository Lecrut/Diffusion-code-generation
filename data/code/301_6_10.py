import json

def is_valid_date(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return False
    month, day, year = (int(month), int(day), int(year))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    return True

def convert_date(date_str):
    month, day, year = date_str.split('-')
    new_date = f'{year}/{month}/{day}'
    return new_date

def convert_dates_in_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    if not isinstance(data, dict) and (not isinstance(data, list)):
        raise ValueError('Invalid JSON format')

    def replace_dates(obj):
        if isinstance(obj, str) and is_valid_date(obj):
            return convert_date(obj)
        elif isinstance(obj, dict):
            return {key: replace_dates(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [replace_dates(item) for item in obj]
        else:
            return obj
    converted_data = replace_dates(data)
    with open(json_file_path, 'w') as file:
        json.dump(converted_data, file, indent=4)
if __name__ == '__main__':
    sample_json = '{"event": "Conference", "date": "2023-12-31"}'
    sample_date = '2023-12-31'
    if is_valid_date(sample_date):
        print(f'Valid date: {sample_date}')
    converted_sample_date = convert_date(sample_date)
    print(f'Converted date: {converted_sample_date}')
    sample_json_data = json.loads(sample_json)
    new_json_data = replace_dates(sample_json_data)
    print('Updated JSON data:', json.dumps(new_json_data, indent=4))