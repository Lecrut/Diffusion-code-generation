def convert_volume(value, unit):
    conversions_to_liters = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'oz': 0.0295735,
        'tsp': 0.00492892,
        'tbsp': 0.0147868
    }

    if unit not in conversions_to_liters:
        raise ValueError(f"Unsupported unit: {unit}")

    liters = value * conversions_to_liters[unit]

    return liters

if __name__ == '__main__':
    result = convert_volume(5, 'gal')
    print(result)