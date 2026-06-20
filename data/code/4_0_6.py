def convert_distance(value, from_unit, to_unit):
    valid_units = ['m', 'km', 'mi', 'miles', 'kilometers', 'meters']
    normalized_from = from_unit.lower().replace(' ', '_')
    normalized_to = to_unit.lower().replace(' ', '_')
    
    if normalized_from not in valid_units and normalized_from not in ['meters', 'kilometers', 'miles']:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if normalized_to not in valid_units and normalized_to not in ['meters', 'kilometers', 'miles']:
        raise ValueError(f"Invalid target unit: {to_unit}")
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Value must be a non-negative number")
    
    if normalized_from in ['m', 'meters']:
        base_meters = value
    elif normalized_from in ['km', 'kilometers']:
        base_meters = value * 1000
    elif normalized_from in ['mi', 'miles']:
        base_meters = value * 1609.34
    
    if normalized_to in ['m', 'meters']:
        return base_meters
    elif normalized_to in ['km', 'kilometers']:
        return base_meters / 1000
    elif normalized_to in ['mi', 'miles']:
        return base_meters / 1609.34

if __name__ == '__main__':
    print(convert_distance(100, 'm', 'km'))
    print(convert_distance(1, 'km', 'mi'))
    print(convert_distance(5, 'miles', 'meters'))
    print(convert_distance(0, 'm', 'mi'))