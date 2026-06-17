import math
def convert_measurements(measurements, target_unit):
    conversion_factors = {
        "meter": 1.0,
        "m": 1.0,
        "meters": 1.0,
        "foot": 0.3048,
        "ft": 0.3048,
        "feet": 0.3048,
        "inch": 0.0254,
        "in": 0.0254,
        "inches": 0.0254
    }
    if target_unit not in conversion_factors:
        raise ValueError(f"Invalid target unit: {target_unit}")
    converted_results = []
    for value, unit in measurements:
        if unit not in conversion_factors:
            raise ValueError(f"Invalid unit found: {unit} for value {value}")
        if unit == target_unit:
            converted_value = value
        else:
            value_in_meters = value * conversion_factors[unit]
            if target_unit == "meter" or target_unit == "m":
                converted_value = value_in_meters
            elif target_unit == "foot" or target_unit == "ft" or target_unit == "feet":
                converted_value = value_in_meters / conversion_factors["foot"]
            elif target_unit == "inch" or target_unit == "in" or target_unit == "inches":
                converted_value = value_in_meters / conversion_factors["inch"]
            else:
                raise ValueError(f"Unsupported conversion path from {unit} to {target_unit}")
        converted_results.append(round(converted_value, 4))
    return converted_results
if __name__ == '__main__':
    sample_measurements = [
        (10, "m"),
        (5, "feet"),
        (200, "inch"),
        (1.5, "meters"),
        (100, "ft")
    ]
    target = "meters"
    try:
        results = convert_measurements(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print("Converted results:")
        for original, converted in zip(sample_measurements, results):
            print(f"Value {original[0]} {original[1]} -> {converted} {target}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing Error Handling ---")
    invalid_measurements = [(10, "m"), (5, "furlongs")]
    try:
        convert_measurements(invalid_measurements, "meters")
    except ValueError as e:
        print(f"Successfully caught expected error for invalid unit: {e}")
    try:
        convert_measurements(sample_measurements, "lightyears")
    except ValueError as e:
        print(f"Successfully caught expected error for invalid target unit: {e}")