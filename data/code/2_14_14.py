def convert_to_milliliters(measurements):
    conversion_factors = {
        'liters': 1000.0,
        'gallons': 3785.411784,
        'cubic_inches': 16.387064
    }

    results = []
    for value, unit in measurements:
        unit_lower = unit.lower()
        if unit_lower in conversion_factors:
            converted = value * conversion_factors[unit_lower]
            if converted < 0:
                results.append(0.0)
            else:
                results.append(converted)
        else:
            results.append(0.0)

    return results

if __name__ == '__main__':
    sample_measurements = [
        (1.0, 'liters'),
        (0.5, 'gallons'),
        (10.0, 'cubic_inches'),
        (0.0, 'liters'),
        (-5.0, 'gallons'),
        (2.5, 'invalid_unit')
    ]
    print(convert_to_milliliters(sample_measurements))