import json
def convert_temperatures(data):
    fahrenheit_to_celsius = lambda x: (x - 32) * 5 / 9
    celsius_to_fahrenheit = lambda x: (x * 9 / 5) + 32
    kelvin_to_celsius = lambda x: x - 273.15
    mapping_strategy = {
        'f': fahrenheit_to_celsius,
        'c': celsius_to_fahrenheit,
        'k': kelvin_to_celsius
    }
    return [mapping_strategy[reading['scale']](reading['value']) for reading in data]
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'location': 'NYC', 'value': 75.0, 'scale': 'f'},
        {'id': 2, 'location': 'London', 'value': 20.0, 'scale': 'c'},
        {'id': 3, 'location': 'Moscow', 'value': 294.15, 'scale': 'k'}
    ]
    converted_data = convert_temperatures(sample_data)
    output_dict = {i: {'original': sample_data[i], 'converted_celsius': c} for i, c in enumerate(converted_data)}
    print(json.dumps(output_dict))