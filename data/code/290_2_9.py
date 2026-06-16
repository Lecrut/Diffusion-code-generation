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
        return mass * 1000
    elif target_unit == 'lb':
        return mass * 2.20462
    else:
        if target_unit in conversion_factors:
            return mass * conversion_factors[target_unit]
        else:
            raise ValueError("Unsupported target unit")
if __name__ == '__main__':
    mass_value = 5.0
    target_unit_kg = 'kg'
    target_unit_g = 'g'
    target_unit_lb = 'lb'
    print(f"{mass_value} kg converted to {target_unit_kg}: {convert_mass(mass_value, target_unit_kg)}")
    print(f"{mass_value} kg converted to {target_unit_g}: {convert_mass(mass_value, target_unit_g)}")
    print(f"{mass_value} kg converted to {target_unit_lb}: {convert_mass(mass_value, target_unit_lb)}")
    try:
        convert_mass(10, 'ton')
    except ValueError as e:
        print(f"Error caught: {e}")