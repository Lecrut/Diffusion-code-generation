import json

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    conversion_factors = {
        'kg': 2.20462,
        'lbs': 1.0,
        'oz': 0.0625
    }
    
    for item in data:
        if 'weight' in item and isinstance(item['weight'], dict):
            unit = item['weight']['unit']
            value = item['weight']['value']
            converted_value = value * conversion_factors[unit]
            item['weight'] = {'unit': 'lbs', 'value': converted_value}
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_input = """
    [
        {"id": 1, "weight": {"unit": "kg", "value": 70}},
        {"id": 2, "weight": {"unit": "lbs", "value": 150}},
        {"id": 3, "weight": {"unit": "oz", "value": 160}}
    ]
    """
    with open('sample_input.json', 'w') as file:
        file.write(sample_input)
    
    convert_weights('sample_input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
        print(json.dumps(output_data, indent=4))