def convert_to_milliliters(volumes):
    factors = {
        'liters': 1000.0,
        'gallons': 3785.411784,
        'cubic_inches': 16.387064,
        'milliliters': 1.0
    }
    results = []
    for value, unit in volumes:
        if value < 0:
            results.append((abs(value), unit))
        elif value == 0:
            results.append((0.0, unit))
        else:
            factor = factors.get(unit)
            if factor is None:
                raise ValueError(f"Unsupported unit: {unit}")
            results.append((value * factor, 'milliliters'))
    return results

if __name__ == '__main__':
    sample_volumes = [
        (1.5, 'liters'),
        (2.0, 'gallons'),
        (10.0, 'cubic_inches'),
        (0.0, 'milliliters'),
        (-5.0, 'liters')
    ]
    converted = convert_to_milliliters(sample_volumes)
    for val, unit in converted:
        print(f"{val} {unit}")