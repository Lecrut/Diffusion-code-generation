def convert_mass(mass, target_unit):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'mg': 0.000001
    }
    if target_unit in conversion_factors:
        return mass * conversion_factors[target_unit]
    else:
        raise ValueError("Unsupported target unit")
if __name__ == '__main__':
    mass_value = 500
    target_unit_kg = 'kg'
    target_unit_g = 'g'
    target_unit_lb = 'lb'
    result_kg = convert_mass(mass_value, target_unit_kg)
    result_g = convert_mass(mass_value, target_unit_g)
    result_lb = convert_mass(mass_value, target_unit_lb)
    print(f"Mass: {mass_value} kg")
    print(f"Converted to grams: {result_g}")
    print(f"Converted to pounds: {result_lb}")