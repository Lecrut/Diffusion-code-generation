LITERS_TO_MILLILITERS = 1000.0
GALLONS_TO_MILLILITERS = 3785.41
CUBIC_INCHES_TO_MILLILITERS = 16.387064

def convert_volumes_to_milliliters(measurements):
    converted = []
    for value, unit in measurements:
        if value < 0:
            converted.append(0.0)
        elif value == 0:
            converted.append(0.0)
        elif unit.lower() in ('l', 'liter', 'liters'):
            converted.append(value * LITERS_TO_MILLILITERS)
        elif unit.lower() in ('gal', 'gallon', 'gallons'):
            converted.append(value * GALLONS_TO_MILLILITERS)
        elif unit.lower() in ('in3', 'cubic inch', 'cubic inches', 'cubicin'):
            converted.append(value * CUBIC_INCHES_TO_MILLILITERS)
        else:
            converted.append(0.0)
    return converted

if __name__ == '__main__':
    sample_measurements = [
        (1.0, 'liters'),
        (0.5, 'gallons'),
        (10.0, 'cubic inches'),
        (0.0, 'liters'),
        (-5.0, 'gallons'),
        (2.5, 'L'),
        (100.0, 'in3')
    ]
    result = convert_volumes_to_milliliters(sample_measurements)
    print(result)