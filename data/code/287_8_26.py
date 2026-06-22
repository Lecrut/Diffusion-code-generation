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

def process_weights(data):
    for item in data:
        if 'weight' in item and isinstance(item['weight'], dict):
            try:
                converted_value = convert_weight(item['weight']['value'], item['weight']['unit'])
                item['weight'] = {'unit': 'lbs', 'value': converted_value}
            except ValueError as e:
                print(e)
    return data

def write_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'weight': {'value': 1.0, 'unit': 'kg'}},
        {'weight': {'value': 2.0, 'unit': 'oz'}},
        {'weight': {'value': 3.5, 'unit': 'lbs'}}
    ]
    output_file = 'converted_weights.json'
    result_data = process_weights(sample_data)
    write_json(result_data, output_file)
    print(f"Converted data written to {output_file}")