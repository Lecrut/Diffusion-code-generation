def convert_distance(value: float, unit_from: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be a number.')
    if not isinstance(unit_from, str):
        raise TypeError('Unit must be a string.')
    unit_from_lower = unit_from.lower().strip()
    if unit_from_lower == 'meters' or unit_from_lower == 'meter' or unit_from_lower == 'm':
        meters = value
    elif unit_from_lower == 'kilometers' or unit_from_lower == 'kilometer' or unit_from_lower == 'km':
        meters = value * 1000.0
    elif unit_from_lower == 'miles' or unit_from_lower == 'mile' or unit_from_lower == 'mi':
        meters = value * 1609.344
    elif unit_from_lower == 'feet' or unit_from_lower == 'foot' or unit_from_lower == 'ft':
        meters = value * 0.3048
    else:
        raise ValueError(f'Unsupported unit: {unit_from}')
    if meters < 0:
        raise ValueError('Distance cannot be negative.')
    return round(meters, 6)

def get_all_units() -> dict:
    return {'meters': 1.0, 'kilometers': 1000.0, 'miles': 1609.344, 'feet': 0.3048}
if __name__ == '__main__':
    units = get_all_units()
    value = 1.0
    for target_unit, factor in units.items():
        result = convert_distance(value, target_unit)
        print(f'{value} {target_unit} = {result} meters')