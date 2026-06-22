def convert_distance(value, from_unit, to_unit):
    if value is None or from_unit is None or to_unit is None:
        raise ValueError("Arguments cannot be None")
    
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
        
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Units must be strings")

    to_meters = {
        'm': 1.0,
        'meter': 1.0,
        'meters': 1.0,
        'km': 1000.0,
        'kilometer': 1000.0,
        'kilometers': 1000.0,
        'cm': 0.01,
        'centimeter': 0.01,
        'centimeters': 0.01,
        'mm': 0.001,
        'millimeter': 0.001,
        'millimeters': 0.001,
        'mi': 1609.344,
        'mile': 1609.344,
        'miles': 1609.344,
        'in': 0.0254,
        'inch': 0.0254,
        'inches': 0.0254,
        'ft': 0.3048,
        'foot': 0.3048,
        'feet': 0.3048,
        'yd': 0.9144,
        'yard': 0.9144,
        'yards': 0.9144
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in to_meters:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit_lower not in to_meters:
        raise ValueError(f"Unknown target unit: {to_unit}")

    meters = value * to_meters[from_unit_lower]
    
    if to_meters[to_unit_lower] == 0:
        raise ZeroDivisionError("Cannot convert to a unit with zero magnitude")

    result = meters / to_meters[to_unit_lower]
    
    if result == 0.0 and value != 0.0:
        if abs(result) < 1e-15:
             return 0.0
             
    return result

if __name__ == '__main__':
    print(convert_distance(100, 'm', 'km'))
    print(convert_distance(1, 'mile', 'meter'))
    print(convert_distance(5.5, 'ft', 'cm'))
    print(convert_distance(0, 'm', 'km'))