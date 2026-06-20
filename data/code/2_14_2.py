LITERS_TO_MILLILITERS = 1000.0
GALLONS_TO_MILLILITERS = 3785.411784
CUBIC_INCHES_TO_MILLILITERS = 16.387064

def convert_to_milliliters(measurements):
    converted = []
    for value, unit in measurements:
        if value < 0:
            converted.append(0.0)
        elif value == 0:
            converted.append(0.0)
        else:
            if unit == 'liters':
                converted.append(value * LITERS_TO_MILLILITERS)
            elif unit == 'gallons':
                converted.append(value * GALLONS_TO_MILLILITERS)
            elif unit == 'cubic_inches':
                converted.append(value * CUBIC_INCHES_TO_MILLILITERS)
            else:
                converted.append(0.0)
    return converted

if __name__ == '__main__':
    sample_measurements = [
        (1.0, 'liters'),
        (2.0, 'gallons'),
        (3.0, 'cubic_inches'),
        (0.0, 'liters'),
        (-1.0, 'gallons'),
        (5.5, 'liters'),
        (100.0, 'cubic_inches'),
        (0.5, 'gallons')
    ]
    result = convert_to_milliliters(sample_measurements)
    print(result)