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
        raise ValueError(f"Invalid target unit specified: {target_unit}. Target must be a metric unit.")
    results = []
    for measurement, unit in measurements:
        unit = unit.lower().strip()
        if unit not in conversion_factors:
            raise ValueError(f"Invalid unit encountered: {unit}")
        value = measurement
        factor = conversion_factors[unit]
        if target_unit == "meter":
            converted_value = value * factor
            results.append(converted_value)
        else:
            raise NotImplementedError("Only conversion to meters is supported by this function.")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "m"),
        (5, "feet"),
        (120, "inch"),
        (3.5, "meters"),
        (100, "yard")                          
    ]
    target = "meter"
    try:
        converted_values = convert_measurements(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted values to {target}: {converted_values}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    except NotImplementedError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")