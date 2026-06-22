import json

def convert_date_format(date_str):
    return date_str.split('-')[::-1].join('/')

def process_json_file(input_path, output_path):
    with open(input_path, 'r') as file:
        data = json.load(file)
    
    if isinstance(data, dict):
        for key in data:
            if isinstance(data[key], str) and len(data[key]) == 10 and data[key].count('-') == 2:
                data[key] = convert_date_format(data[key])
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], str) and len(data[i]) == 10 and data[i].count('-') == 2:
                data[i] = convert_date_format(data[i])
    
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_json = '{"events": ["2023-12-31", "2024-01-05"], "meeting": {"date": "2022-07-15"}}'
    with open('temp_input.json', 'w') as file:
        json.dump(json.loads(input_json), file)
    
    process_json_file('temp_input.json', 'temp_output.json')
    
    with open('temp_output.json', 'r') as file:
        print(file.read())