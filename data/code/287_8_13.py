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
        weight_value, weight_unit = item['weight'].split()
        weight_value = float(weight_value)
        converted_weight = weight_value * conversion_factors[weight_unit]
        item['weight'] = f"{converted_weight:.2f} lbs"
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_data = [
        {'item': 'apple', 'weight': '1 kg'},
        {'item': 'banana', 'weight': '0.5 lbs'},
        {'item': 'chocolate', 'weight': '2 oz'}
    ]
    
    with open('input.json', 'w') as file:
        json.dump(input_data, file)
    
    convert_weights('input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
    
    print(json.dumps(output_data, indent=4))