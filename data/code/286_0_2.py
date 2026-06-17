import math
def convert_to_meters(value, unit):
    if unit == "meters":
        return value
    elif unit == "kilometers":
        return value * 1000.0
    elif unit == "miles":
        return value * 1609.344
    elif unit == "feet":
        return value * 0.3048
    elif unit == "inches":
        return value * 0.0254
    else:
        raise ValueError("Unknown unit")
if __name__ == '__main__':
    measurements = [
        (10, "meters"),
        (2.5, "kilometers"),
        (5, "miles"),
        (100, "feet"),
        (120, "inches")
    ]
    results = []
    for value, unit in measurements:
        try:
            meters = convert_to_meters(value, unit)
            results.append((value, unit, meters))
        except ValueError as e:
            results.append((value, unit, f"Error: {e}"))
    for value, unit, meters in results:
        print(f"{value} {unit} is equal to {meters:.4f} meters")