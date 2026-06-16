import sys
def convert_mass(value, unit):
    if unit == 'kg':
        return value
    elif unit == 'g':
        return value / 1000
    elif unit == 'lb':
        return value * 2.20462
    else:
        raise ValueError("Invalid unit specified. Must be 'kg', 'g', or 'lb'.")
if __name__ == '__main__':
    mass_kg = 5.5
    unit_kg = 'kg'
    result = convert_mass(mass_kg, unit_kg)
    print(f"Input Mass: {mass_kg} {unit_kg}")
    print(f"Converted Mass: {result}")
    mass_g = 2500
    unit_g = 'g'
    result = convert_mass(mass_g, unit_g)
    print(f"Input Mass: {mass_g} {unit_g}")
    print(f"Converted Mass: {result}")
    mass_lb = 150.0
    unit_lb = 'lb'
    result = convert_mass(mass_lb, unit_lb)
    print(f"Input Mass: {mass_lb} {unit_lb}")
    print(f"Converted Mass: {result}")
    try:
        convert_mass(10, 'oz')
    except ValueError as e:
        print(f"Error caught: {e}")