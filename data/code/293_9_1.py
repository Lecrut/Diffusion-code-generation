import json
def system_converter(input_data, conversion_map):
    output_data = {}
    for key, value in input_data.items():
        if key in conversion_map:
            output_data[conversion_map[key]] = value
        else:
            output_data[key] = f"Conversion Error: Key '{key}' not found in map"
    return output_data
if __name__ == '__main__':
    input_values = {
        "USD": 100,
        "EUR": 85.5,
        "GBP": 92.15,
        "JPY": 15000
    }
    conversion_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.80,
        "JPY": 150.0
    }
    converted_results = system_converter(input_values, conversion_rates)
    print(json.dumps(converted_results, indent=4))