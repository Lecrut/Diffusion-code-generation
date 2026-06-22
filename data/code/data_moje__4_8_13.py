def convert_distance(value, from_unit, to_unit):
    conversion_factors = {
        ('km', 'mi'): 0.621371,
        ('mi', 'km'): 1.60934,
        ('km', 'km'): 1.0,
        ('mi', 'mi'): 1.0,
    }
    key = (from_unit.lower(), to_unit.lower())
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    return value * conversion_factors[key]

if __name__ == '__main__':
    result_km_to_mi = convert_distance(100, 'km', 'mi')
    result_mi_to_km = convert_distance(50, 'mi', 'km')
    print(result_km_to_mi)
    print(result_mi_to_km)