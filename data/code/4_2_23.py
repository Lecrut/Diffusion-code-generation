def convert_distance(distance, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}
    if unit not in conversion_factors:
        raise ValueError('Unsupported unit')
    meters = distance * conversion_factors[unit]
    converted_distances = {}
    for u, factor in conversion_factors.items():
        converted_distances[u] = meters / factor
    return converted_distances
if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    result = convert_distance(sample_distance, sample_unit)
    print(result)