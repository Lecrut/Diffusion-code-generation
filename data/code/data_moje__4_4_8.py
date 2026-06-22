def convert_distance(distance: float, target_unit: str) -> float:
    to_meters = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344, 'ft': 0.3048}
    from_meters = {k: 1.0 / v for k, v in to_meters.items()}
    if target_unit not in to_meters:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    if distance == 0.0:
        return 0.0
    meters = distance * to_meters.get(target_unit, 0)
    value_in_target = distance / to_meters[target_unit]
    return value_in_target
if __name__ == '__main__':
    result = convert_distance(5000, 'km')
    print(result)
    result2 = convert_distance(1, 'mi')
    print(result2)
    result3 = convert_distance(100, 'ft')
    print(result3)