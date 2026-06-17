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
        if unit_lower != "meter" and unit_lower != "m":
            value = measurement * conversion_factors[unit_lower]
        results.append(value)
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "meters"),
        (5, "feet"),
        (12, "inches"),
        (20, "m"),
        (3, "miles")                          
    ]
    target = "meters"
    try:
        converted_values = convert_measurements(sample_measurements, target)
        print(f"Target Unit: {target}")
        for original, converted in zip(sample_measurements, converted_values):
            print(f"Original: {original} {sample_measurements[0][1] if sample_measurements[0][1] == 'meters' else sample_measurements[0][1]} -> Converted: {converted:.4f} {target}")
    except ValueError as e:
        print(f"Error during conversion: {e}")