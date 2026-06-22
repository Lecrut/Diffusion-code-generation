def convert_distance(distance, unit):
    units = {'m', 'km', 'mi', 'ft', 'in'}
    if unit not in units:
        raise ValueError(f"Unsupported unit: {unit}. Supported: {units}")

    if distance < 0:
        raise ValueError("Distance cannot be negative")

    to_meters = {
        'm': 1,
        'km': 1000,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254
    }

    meters = distance * to_meters[unit]

    from_meters = {
        'm': 1,
        'km': 0.001,
        'mi': 1 / 1609.344,
        'ft': 1 / 0.3048,
        'in': 1 / 0.0254
    }

    result = {}
    for u in units:
        if u != unit:
            result[u] = meters * from_meters[u]

    return result

if __name__ == '__main__':
    print(convert_distance(1, 'km'))
    print(convert_distance(5, 'mi'))
    print(convert_distance(100, 'ft'))
    print(convert_distance(12, 'in'))