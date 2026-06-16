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
        unit_lower = unit.lower()
        if unit_lower not in conversion_factors:
            raise ValueError(f"Invalid unit encountered: {unit}")
        value = measurement
        factor = conversion_factors[unit_lower]
        if target_unit == "meter":
            converted_value = value * factor
            results.append(converted_value)
        else:
            results.append(value)                                                                            
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "m"),
        (5, "feet"),
        (120, "inch"),
        (3.28084, "ft"),
        (1.5, "meters")
    ]
    target = "meter"
    try:
        converted_values = convert_measurements(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print("Converted values (in meters):")
        for original, converted in zip(sample_measurements, converted_values):
            print(f"{original} {sample_measurements[0][1] if sample_measurements[0][1] != target else 'm'} -> {converted:.4f} m")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing Invalid Unit Handling ---")
    invalid_measurements = [
        (10, "m"),
        (5, "parsecs")
    ]
    try:
        convert_measurements(invalid_measurements, target)
    except ValueError as e:
        print(f"Successfully caught expected error for invalid unit: {e}")