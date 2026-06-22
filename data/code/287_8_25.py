import json

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    conversion_factors = {'kg': 2.20462, 'lbs': 1, 'oz': 0.0625}
    
    for item in data:
        if 'weight' in item and 'unit' in item:
            weight = item['weight']
            unit = item['unit']
            new_weight = weight * conversion_factors[unit]
            item['weight'] = new_weight
            item['unit'] = 'lbs'
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_data = [
        {'weight': 100, 'unit': 'kg'},
        {'weight': 200, 'unit': 'lbs'},
        {'weight': 32, 'unit': 'oz'}
    ]
    
    with open('input.json', 'w') as file:
        json.dump(input_data, file)
    
    convert_weights('input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
        print(json.dumps(output_data, indent=4))