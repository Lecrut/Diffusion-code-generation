def convert_volume(value, target_unit):
    conversion_rates = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'fl_oz': 0.0295735,
        'cup': 0.236588,
        'pint': 0.473176,
        'quart': 0.946353
    }

    if target_unit not in conversion_rates:
        raise ValueError(f"Unsupported unit: {target_unit}")

    base_value = value / conversion_rates[target_unit] if target_unit != 'L' else value
    return base_value

if __name__ == '__main__':
    print(convert_volume(1000, 'L'))
    print(convert_volume(1, 'm3'))
    print(convert_volume(5, 'gal'))
    print(convert_volume(250, 'ml'))
    print(convert_volume(16, 'fl_oz'))
    print(convert_volume(2, 'cup'))
    print(convert_volume(1, 'pint'))
    print(convert_volume(1, 'quart'))