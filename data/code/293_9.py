import json
def system_converter(input_data, conversion_map):
    output_data = {}
    for key, value in input_data.items():
        if key in conversion_map:
            output_data[key] = conversion_map[key]
        else:
            output_data[key] = f"Conversion not found for {key}"
    return output_data
if __name__ == '__main__':
    input_system_data = {
        "temperature_celsius": 25.0,
        "speed_kph": 60.0,
        "distance_km": 100.0
    }
    conversion_rules = {
        "temperature_celsius": "Fahrenheit",
        "speed_kph": "mph",
        "distance_km": "miles"
    }
    converted_data = system_converter(input_system_data, conversion_rules)
    print(json.dumps(converted_data, indent=4))