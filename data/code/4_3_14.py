def convert_length(value, unit_from, unit_to):
    to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    if unit_from not in to_meters or unit_to not in to_meters:
        raise ValueError(f"Unsupported unit: {unit_from} or {unit_to}")
    meters = value * to_meters[unit_from]
    return meters / to_meters[unit_to]

def convert_mass(value, unit_from, unit_to):
    to_kg = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }
    if unit_from not in to_kg or unit_to not in to_kg:
        raise ValueError(f"Unsupported unit: {unit_from} or {unit_to}")
    kg = value * to_kg[unit_from]
    return kg / to_kg[unit_to]

if __name__ == '__main__':
    length_result = convert_length(5, 'km', 'mi')
    print(length_result)
    mass_result = convert_mass(1, 'lb', 'kg')
    print(mass_result)