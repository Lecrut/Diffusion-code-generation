def convert_distance(value, unit):
    units = ['m', 'km', 'mi']
    conversions_to_m = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344}
    if unit not in conversions_to_m:
        raise ValueError(f"Unsupported unit: {unit}")
    value_in_m = value * conversions_to_m[unit]
    result = {}
    for u in units:
        if u != unit:
            result[u] = value_in_m / conversions_to_m[u]
    return result

if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = 'km'
    converted = convert_distance(sample_value, sample_unit)
    print(converted)