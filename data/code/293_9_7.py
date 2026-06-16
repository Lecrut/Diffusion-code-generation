import json
def system_converter(input_data, conversion_map):
    output_data = {}
    for key, value in input_data.items():
        if key in conversion_map:
            output_data[key] = conversion_map[key]
        else:
            output_data[key] = f"Conversion Error: Key '{key}' not found in map"
    return output_data
if __name__ == '__main__':
    system_a_data = {
        "temperature_celsius": 25.0,
        "speed_kph": 60.0,
        "distance_km": 100.0
    }
    system_b_map = {
        "temperature_fahrenheit": lambda c: (c * 9/5) + 32,
        "speed_mph": lambda kph: kph * 0.621371,
        "distance_miles": lambda km: km * 0.621371
    }
    converted_data = system_converter(system_a_data, system_b_map)
    print(json.dumps(converted_data, indent=4))