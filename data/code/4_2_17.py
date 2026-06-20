def convert_distance(value, unit):
    m_factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }
    if unit not in m_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    meters = value * m_factors[unit]
    results = {}
    for u, factor in m_factors.items():
        if u == unit:
            results[u] = value
        else:
            results[u] = meters / factor
    return results

if __name__ == '__main__':
    result = convert_distance(1, 'km')
    print(result)
    result2 = convert_distance(5280, 'ft')
    print(result2)