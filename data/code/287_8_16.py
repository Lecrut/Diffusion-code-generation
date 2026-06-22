import json

def is_valid_weight(weight):
    if not isinstance(weight, dict) or 'value' not in weight or 'unit' not in weight:
        return False
    if not isinstance(weight['value'], (int, float)) or weight['value'] < 0:
        return False
    if weight['unit'] not in ['kg', 'lbs', 'oz']:
        return False
    return True

def convert_weight_to_pounds(weight):
    conversion_factors = {
        'kg': 2.20462,
        'lbs': 1,
        'oz': 0.0625
    }
    if is_valid_weight(weight):
        return weight['value'] * conversion_factors[weight['unit']]
    raise ValueError("Invalid weight data")

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    for item in data:
        if 'weight' in item and is_valid_weight(item['weight']):
            item['weight'] = {'unit': 'lbs', 'value': convert_weight_to_pounds(item['weight'])}
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_data = [
        {
            "item": "apple",
            "weight": {"unit": "kg", "value": 0.5}
        },
        {
            "item": "banana",
            "weight": {"unit": "oz", "value": 16}
        }
    ]
    
    with open('input.json', 'w') as file:
        json.dump(input_data, file)
    
    convert_weights('input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        result = json.load(file)
    print(result)