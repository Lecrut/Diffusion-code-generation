LITER_TO_MILLILITERS = 1000.0
GALLON_TO_MILLILITERS = 3785.411784
CUBIC_INCH_TO_MILLILITERS = 16.387064

def convert_to_milliliters(volume, unit):
    if volume < 0:
        raise ValueError("Volume must be non-negative")
    if unit == "liters":
        return volume * LITER_TO_MILLILITERS
    elif unit == "gallons":
        return volume * GALLON_TO_MILLILITERS
    elif unit == "cubic_inches":
        return volume * CUBIC_INCH_TO_MILLILITERS
    else:
        raise ValueError("Unsupported unit")

def convert_all_volumes(measurements):
    results = []
    for volume, unit in measurements:
        try:
            ml_value = convert_to_milliliters(volume, unit)
            results.append(ml_value)
        except ValueError:
            results.append(None)
    return results

if __name__ == '__main__':
    sample_measurements = [
        (1.0, "liters"),
        (0.5, "gallons"),
        (10.0, "cubic_inches"),
        (0.0, "liters"),
        (-1.0, "gallons"),
        (2.5, "unknown_unit")
    ]
    converted_values = convert_all_volumes(sample_measurements)
    print(converted_values)