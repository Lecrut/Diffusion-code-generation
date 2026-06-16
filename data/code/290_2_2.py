def convert_mass(mass, target_unit):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'mg': 0.000001
    }
    if target_unit not in conversion_factors:
        raise ValueError("Unsupported target unit")
    mass_in_kg = mass
    if target_unit == 'kg':
        return mass_in_kg
    elif target_unit == 'g':
        return mass_in_kg / 1000.0
    elif target_unit == 'lb':
        return mass_in_kg / 0.453592
    elif target_unit == 'mg':
        return mass_in_kg * 1000000.0
    else:
        raise ValueError("Invalid unit specified")
if __name__ == '__main__':
    mass_value = 5.0
    target_unit_kg = 'kg'
    target_unit_g = 'g'
    target_unit_lb = 'lb'
    target_unit_mg = 'mg'
    result_kg = convert_mass(mass_value, target_unit_kg)
    result_g = convert_mass(mass_value, target_unit_g)
    result_lb = convert_mass(mass_value, target_unit_lb)
    result_mg = convert_mass(mass_value, target_unit_mg)
    print(f"Mass: {mass_value} kg")
    print(f"Converted to kg: {result_kg}")
    print(f"Converted to g: {result_g}")
    print(f"Converted to lb: {result_lb}")
    print(f"Converted to mg: {result_mg}")