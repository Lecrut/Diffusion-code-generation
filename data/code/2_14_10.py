LITERS_TO_MILLILITERS = 1000.0
GALLONS_TO_MILLILITERS = 3785.411784
CUBIC_INCHES_TO_MILLILITERS = 16.387064

def convert_to_milliliters(measurements):
    converted = []
    for value, unit in measurements:
        if unit == 'liters':
            result = value * LITERS_TO_MILLILITERS
        elif unit == 'gallons':
            result = value * GALLONS_TO_MILLILITERS
        elif unit == 'cubic_inches':
            result = value * CUBIC_INCHES_TO_MILLILITERS
        else:
            result = 0.0
        converted.append(round(result, 6))
    return converted

if __name__ == '__main__':
    sample_data = [
        (1.5, 'liters'),
        (0.5, 'gallons'),
        (10, 'cubic_inches'),
        (0, 'liters'),
        (-2, 'gallons'),
        (100, 'cubic_inches')
    ]
    result = convert_to_milliliters(sample_data)
    print(result)