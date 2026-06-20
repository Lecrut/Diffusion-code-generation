def convert_distance(distance, unit):
    units = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344, 'ft': 0.3048, 'in': 0.0254, 'cm': 0.01}
    if unit not in units:
        raise ValueError(f"Unsupported unit: {unit}")
    meters = distance * units[unit]
    results = {}
    for u, factor in units.items():
        if u != unit:
            results[u] = meters / factor
    return results

if __name__ == '__main__':
    result = convert_distance(5.0, 'km')
    print(result)