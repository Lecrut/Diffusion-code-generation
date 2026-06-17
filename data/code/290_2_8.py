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
    else:
        return mass * conversion_factors[target_unit]
if __name__ == '__main__':
    mass_value = 5.0
    target_unit_1 = 'kg'
    target_unit_2 = 'g'
    target_unit_3 = 'lb'
    target_unit_4 = 'mg'
    result_1 = convert_mass(mass_value, target_unit_1)
    result_2 = convert_mass(mass_value, target_unit_2)
    result_3 = convert_mass(mass_value, target_unit_3)
    result_4 = convert_mass(mass_value, target_unit_4)
    print(f"Mass: {mass_value} kg")
    print(f"Converted to kg: {result_1}")
    print(f"Converted to g: {result_2}")
    print(f"Converted to lb: {result_3}")
    print(f"Converted to mg: {result_4}")