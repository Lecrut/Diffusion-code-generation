def convert_distance(value, from_unit, to_unit):
    conversion_factors = {
        ('m', 'm'): 1.0,
        ('m', 'km'): 0.001,
        ('m', 'mi'): 0.000621371,
        ('km', 'm'): 1000.0,
        ('km', 'km'): 1.0,
        ('km', 'mi'): 0.621371,
        ('mi', 'm'): 1609.34,
        ('mi', 'km'): 1.60934,
        ('mi', 'mi'): 1.0,
    }
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    valid_units = ['m', 'km', 'mi']
    if value < 0:
        raise ValueError("Distance cannot be negative")
    if from_unit not in valid_units:
        raise ValueError(f"Invalid source unit: {from_unit}. Must be one of {valid_units}")
    if to_unit not in valid_units:
        raise ValueError(f"Invalid target unit: {to_unit}. Must be one of {valid_units}")
    factor = conversion_factors[(from_unit, to_unit)]
    return value * factor

if __name__ == '__main__':
    print(convert_distance(1000, 'm', 'km'))
    print(convert_distance(1, 'km', 'm'))
    print(convert_distance(1, 'mi', 'km'))
    print(convert_distance(5, 'km', 'mi'))
    print(convert_distance(100, 'm', 'mi'))