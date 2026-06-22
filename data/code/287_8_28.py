import json

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    for item in data:
        if 'weight' in item:
            weight_value = item['weight']
            weight_unit = item.get('unit', 'kg')
            
            if weight_unit == 'kg':
                item['weight'] = weight_value * 2.20462
            elif weight_unit == 'oz':
                item['weight'] = weight_value / 16
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_input = """
    [
        {"item": "apple", "weight": 0.5, "unit": "kg"},
        {"item": "banana", "weight": 16, "unit": "oz"}
    ]
    """
    with open('sample_input.json', 'w') as file:
        file.write(sample_input)
    
    convert_weights('sample_input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
        print(json.dumps(output_data, indent=4))