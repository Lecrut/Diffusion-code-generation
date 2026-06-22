import json

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    converted_data = []
    for item in data:
        weight = item['weight']
        unit = item['unit']
        if unit == 'kg':
            converted_weight = weight * 2.20462
        elif unit == 'oz':
            converted_weight = weight / 16
        else:
            converted_weight = weight
        converted_data.append({'weight': converted_weight, 'unit': 'lbs'})
    
    with open(output_file, 'w') as file:
        json.dump(converted_data, file, indent=4)

if __name__ == '__main__':
    input_json = '[{"weight": 10, "unit": "kg"}, {"weight": 32, "unit": "oz"}]'
    with open('input.json', 'w') as file:
        file.write(input_json)
    
    convert_weights('input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
        print(output_data)