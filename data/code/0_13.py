import sys
def convert_measurement(value, unit):
    if unit == "km":
        meters = value * 1000
        feet = meters * 3.28084
        return meters, feet
    elif unit == "m":
        meters = value
        feet = value / 3.28084
        return meters, feet
    elif unit == "ft":
        meters = value * 0.3048
        feet = value
        return meters, feet
    else:
        raise ValueError("Unsupported unit")
if __name__ == '__main__':
    measurements = [10.5, 2.0, 50.0, 1.5]
    unit = "km"
    results = []
    for measure in measurements:
        meters, feet = convert_measurement(measure, unit)
        results.append((measure, meters, feet))
    for original, meters, feet in results:
        print(f"Original {original} {unit}:")
        print(f"  Meters: {meters:.3f}")
        print(f"  Feet: {feet:.3f}")