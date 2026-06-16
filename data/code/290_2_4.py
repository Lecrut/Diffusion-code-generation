def convert_mass(mass, target_unit):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'mg': 0.000001
    }
    if target_unit not in conversion_factors:
        raise ValueError("Unsupported target unit")
    if target_unit == 'kg':
        return mass
    elif target_unit == 'g':
        return mass * 1000.0
    elif target_unit == 'lb':
        return mass / 0.453592
    elif target_unit == 'mg':
        return mass * 1000000.0
    else:
        return mass
if __name__ == '__main__':
    mass_value = 500
    target = 'kg'
    result = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg converted to {target}: {result}")
    mass_value = 2.20462
    target = 'lb'
    result = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg converted to {target}: {result}")
    mass_value = 1000
    target = 'g'
    result = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} g converted to {target}: {result}")
    mass_value = 500000
    target = 'mg'
    result = convert_mass(mass_value, target)
    print(f"Mass: {mass_value} kg converted to {target}: {result}")