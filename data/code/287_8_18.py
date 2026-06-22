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
            weight_value = item['weight']['value']
            weight_unit = item['weight']['unit']
            new_weight = weight_value * conversion_factors[weight_unit]
            item['weight'] = {'value': new_weight, 'unit': 'lbs'}
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_input = """
    [
        {"id": 1, "weight": {"value": 70, "unit": "kg"}},
        {"id": 2, "weight": {"value": 150, "unit": "lbs"}},
        {"id": 3, "weight": {"value": 480, "unit": "oz"}}
    ]
    """
    sample_output = 'output.json'
    
    with open(sample_input, 'w') as file:
        file.write(sample_input)
    
    convert_weights('sample_input.json', sample_output)
    
    with open(sample_output, 'r') as file:
        print(json.load(file))