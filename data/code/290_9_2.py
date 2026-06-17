import sys
def convert_mass(mass, unit):
    if unit == "kg":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass
    elif unit == "g":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass * 1000.0
    elif unit == "lb":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass * 2.2046226218
    else:
        return "Invalid unit"
if __name__ == '__main__':
    mass_data = [
        (10, "kg"),
        (500, "g"),
        (2.2046226218, "lb"),
        (1500, "g"),
        (5, "lb")
    ]
    for mass, unit in mass_data:
        converted = convert_mass(mass, unit)
        print(f"Original: {mass} {unit}")
        print(f"Converted to kg: {convert_mass(mass, unit)}")
        print(f"Converted to g: {convert_mass(mass, unit)}")
        print(f"Converted to lb: {convert_mass(mass, unit)}")
        print("-" * 20)
    print("Program finished.")