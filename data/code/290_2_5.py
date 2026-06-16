def convert_mass(mass, target_unit):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'mg': 0.000001,
        'ton': 1000.0
    }
    if target_unit not in conversion_factors:
        raise ValueError("Unsupported target unit")
    if target_unit == 'kg':
        return mass
    elif target_unit == 'g':
        return mass * 1000.0
    elif target_unit == 'lb':
        return mass * 2.20462
    elif target_unit == 'mg':
        return mass * 1000000.0
    elif target_unit == 'ton':
        return mass / 1000.0
    else:
        return mass
if __name__ == '__main__':
    mass_value = 5
    target = 'kg'
    converted = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg, Converted to {target}: {converted}")
    mass_value = 10
    target = 'g'
    converted = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg, Converted to {target}: {converted}")
    mass_value = 2.20462
    target = 'lb'
    converted = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg, Converted to {target}: {converted}")
    mass_value = 1000
    target = 'ton'
    converted = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg, Converted to {target}: {converted}")