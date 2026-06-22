def convert_volume(value, from_unit, to_unit):
    unit_map = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'gallons': 3.78541,
        'cubic_inches': 0.0163871
    }
    if from_unit not in unit_map or to_unit not in unit_map:
        raise ValueError("Unsupported unit")
    value_in_liters = value * unit_map[from_unit]
    result = value_in_liters / unit_map[to_unit]
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'liters', 'gallons'))
    print(convert_volume(1, 'gallons', 'milliliters'))
    print(convert_volume(1000, 'milliliters', 'cubic_meters'))
    print(convert_volume(1, 'cubic_meters', 'cubic_inches'))
    print(convert_volume(50, 'cubic_inches', 'liters'))