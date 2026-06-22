import json

def convert_weight(value, unit):
    conversion_factors = {
        'kg': 2.20462,
        'lbs': 1.0,
        'oz': 0.0625
    }
    return value * conversion_factors[unit]

def process_data(data):
    for item in data:
        if 'weight' in item and isinstance(item['weight'], dict):
            unit = item['weight']['unit']
            value = item['weight']['value']
            converted_value = convert_weight(value, unit)
            item['weight'] = {'unit': 'lbs', 'value': converted_value}
    return data

def main():
    input_data = [
        {'id': 1, 'name': 'Item1', 'weight': {'value': 2.0, 'unit': 'kg'}},
        {'id': 2, 'name': 'Item2', 'weight': {'value': 16, 'unit': 'oz'}}
    ]
    
    converted_data = process_data(input_data)
    
    with open('output.json', 'w') as file:
        json.dump(converted_data, file, indent=4)

if __name__ == '__main__':
    main()