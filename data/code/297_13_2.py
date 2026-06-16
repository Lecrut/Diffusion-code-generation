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
        if unit in conversion_factors:
            value_in_meters = measurement * conversion_factors[unit]
            results.append(value_in_meters)
        else:
            raise ValueError(f"Invalid unit encountered: {unit}")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, "m"),
        (5, "feet"),
        (120, "inch"),
        (3.5, "meters"),
        (100, "miles")                          
    ]
    target = "meter"
    try:
        converted_values = convert_measurements(sample_measurements, target)
        print(f"Target Unit: {target}")
        print("Converted Measurements (in meters):")
        for original, result in zip(sample_measurements, converted_values):
            print(f"{original} {sample_measurements[1].split()[0]} -> {result:.4f} m")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")