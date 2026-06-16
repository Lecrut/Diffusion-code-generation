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
    if target_unit not in ["meter", "m", "meters"]:
        raise ValueError(f"Invalid target unit specified: {target_unit}")
    results = []
    for value, unit in measurements:
        unit = unit.lower().strip()
        if unit in conversion_factors:
            if target_unit == "meter":
                if unit in ["meter", "m", "meters"]:
                    results.append(value)
                else:
                    try:
                        factor = conversion_factors[unit]
                        converted_value = value * factor
                        results.append(converted_value)
                    except Exception:
                        raise ValueError(f"Error converting {value} from {unit}")
            else:
                raise NotImplementedError("Conversion logic only supports target_unit='meter'")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "meters"),
        (5, "feet"),
        (12, "inches"),
        (2.5, "m"),
        (100, "cm")                     
    ]
    target = "meter"
    try:
        converted_results = convert_measurements(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted results (in meters): {converted_results}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    except NotImplementedError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")