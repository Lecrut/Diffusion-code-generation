def convert_distance(distance, unit):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048,
        'yd': 0.9144,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'nmi': 1852.0
    }

    if unit not in units:
        raise ValueError(f"Unsupported unit: {unit}")

    meters = distance * units[unit]

    result = {}
    for u, factor in units.items():
        result[u] = meters / factor

    return result

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    converted = convert_distance(sample_distance, sample_unit)
    print(converted)