def convert_distance(distance, unit):
    supported_units = ['m', 'km', 'mi', 'ft', 'yd', 'in']
    conversion_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048,
        'yd': 0.9144,
        'in': 0.0254
    }
    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")
    distance_in_meters = distance * conversion_to_meters[unit]
    results = {}
    for u in supported_units:
        results[u] = distance_in_meters / conversion_to_meters[u]
    return results

if __name__ == '__main__':
    sample_distance = 5.0
    sample_unit = 'km'
    converted = convert_distance(sample_distance, sample_unit)
    print(converted)