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
    mass_value = 5
    target_unit_kg = 'kg'
    result_kg = convert_mass(mass_value, target_unit_kg)
    print(f"{mass_value} kg is {result_kg:.4f} g")
    mass_value = 10
    target_unit_lb = 'lb'
    result_lb = convert_mass(mass_value, target_unit_lb)
    print(f"{mass_value} lb is {result_lb:.4f} kg")
    mass_value = 2500
    target_unit_mg = 'mg'
    result_mg = convert_mass(mass_value, target_unit_mg)
    print(f"{mass_value} mg is {result_mg:.1f} g")