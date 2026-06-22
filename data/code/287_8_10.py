import json

def convert_weights(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    conversion_factors = {
        'kg': 2.20462,
        'lbs': 1,
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
    input_data = [
        {
            "id": 1,
            "weight": {"unit": "kg", "value": 70}
        },
        {
            "id": 2,
            "weight": {"unit": "lbs", "value": 154}
        },
        {
            "id": 3,
            "weight": {"unit": "oz", "value": 1600}
        }
    ]
    
    with open('input.json', 'w') as file:
        json.dump(input_data, file)
    
    convert_weights('input.json', 'output.json')
    
    with open('output.json', 'r') as file:
        output_data = json.load(file)
    
    print(output_data)