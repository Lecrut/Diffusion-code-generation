import json

def convert_weight(value, unit):
    conversion_factors = {
        'kg': 2.20462,
        'lbs': 1,
        'oz': 0.0625
    }
    if unit not in conversion_factors:
        raise ValueError(f"Invalid weight unit: {unit}")
    return value * conversion_factors[unit]

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    for item in data:
        if 'weight' in item and isinstance(item['weight'], dict):
            try:
                converted_value = convert_weight(item['weight']['value'], item['weight']['unit'])
                item['weight'] = {'unit': 'lbs', 'value': converted_value}
            except ValueError as e:
                print(f"Error converting weight for item: {e}")
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_data = [
        {'weight': {'value': 10, 'unit': 'kg'}},
        {'weight': {'value': 20, 'unit': 'oz'}},
        {'weight': {'value': 5, 'unit': 'lbs'}}
    ]
    
    with open('input.json', 'w') as file:
        json.dump(input_data, file)
    
    convert_weights('input.json', 'output.json')