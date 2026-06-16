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
    results = []
    for value, unit in measurements:
        if unit not in conversion_factors:
            raise ValueError(f"Invalid unit encountered: {unit}")
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
                raise RuntimeError("Conversion logic error for specific unit path.")
        results.append(round(converted_value, 4))
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "meter"),
        (5, "foot"),
        (300, "cm"),
        (12, "inch"),
        (2.5, "m")
    ]
    target = "meter"
    try:
        converted_results = convert_measurements(sample_measurements, target)
        print(f"Original Measurements: {sample_measurements}")
        print(f"Target Unit: {target}")
        print("Converted Results:")
        for original, converted in zip(sample_measurements, converted_results):
            print(f"Input: {original[0]} {original[1]} -> Output: {converted} {target}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    except RuntimeError as e:
        print(f"Runtime Error during conversion: {e}")