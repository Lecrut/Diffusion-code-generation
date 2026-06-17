def convert_mass(mass, target_unit):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'mg': 0.000001
    }
    if target_unit not in conversion_factors:
        return "Error: Invalid unit"
    if target_unit == 'kg':
        return mass
    else:
        return mass * conversion_factors[target_unit]
if __name__ == '__main__':
    mass_value = 500
    target = 'lb'
    result = convert_mass(mass_value, target)
    print(f"{mass_value} kg is {result:.2f} lb")
    mass_value = 2500
    target = 'g'
    result = convert_mass(mass_value, target)
    print(f"{mass_value} g is {result:.2f} kg")
    mass_value = 10
    target = 'kg'
    result = convert_mass(mass_value, target)
    print(f"{mass_value} kg is {result:.2f} kg")
    mass_value = 500
    target = 'ton'
    result = convert_mass(mass_value, target)
    print(f"{mass_value} kg is {result}")