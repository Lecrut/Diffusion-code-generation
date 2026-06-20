def convert_distance(value, unit):
    units = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344, 'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144}
    if unit not in units:
        raise ValueError("Unsupported unit")
    base_value = value * units[unit]
    result = {}
    for u, factor in units.items():
        if u != unit:
            result[u] = base_value / factor
    return result

if __name__ == '__main__':
    sample_distance = 5.0
    sample_unit = 'km'
    converted = convert_distance(sample_distance, sample_unit)
    print(converted)