def normalize_distance_to_meters(value: float, unit: str) -> float:
    units_to_meters = {'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1.0, 'km': 1000.0, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.344, 'nm': 1e-09, 'um': 1e-06}
    unit_lower = unit.lower()
    if unit_lower not in units_to_meters:
        raise ValueError(f'Unsupported unit: {unit}')
    factor = units_to_meters[unit_lower]
    return value * factor
if __name__ == '__main__':
    samples = [(5, 'km'), (150, 'cm'), (3, 'mi'), (1000, 'mm'), (1, 'm')]
    for val, unit in samples:
        result = normalize_distance_to_meters(val, unit)
        print(f'{val} {unit} = {result} m')