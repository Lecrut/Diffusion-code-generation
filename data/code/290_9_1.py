import sys
def convert_mass(mass, unit):
    if unit == "kg":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass
        else:
            return 0.0
    elif unit == "g":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass * 1000.0
        else:
            return 0.0
    elif unit == "lb":
        if mass == 0:
            return 0.0
        elif mass > 0:
            return mass * 2.20462
        else:
            return 0.0
    else:
        return "Invalid unit"
if __name__ == '__main__':
    mass_to_convert = 100
    unit_to_convert = "kg"
    conversion_steps = 5
    print(f"Starting conversion simulation with sample mass: {mass_to_convert} {unit_to_convert}")
    for i in range(conversion_steps):
        print(f"\n--- Step {i + 1} ---")
        print(f"Current Mass: {mass_to_convert} {unit_to_convert}")
        if unit_to_convert == "kg":
            converted_value = convert_mass(mass_to_convert, "kg")
            print(f"Conversion to kg: {converted_value:.4f} kg")
            mass_to_convert = converted_value
            unit_to_convert = "kg"
        elif unit_to_convert == "g":
            converted_value = convert_mass(mass_to_convert, "g")
            print(f"Conversion to g: {converted_value:.4f} g")
            mass_to_convert = converted_value
            unit_to_convert = "g"
        elif unit_to_convert == "lb":
            converted_value = convert_mass(mass_to_convert, "lb")
            print(f"Conversion to lb: {converted_value:.4f} lb")
            mass_to_convert = converted_value
            unit_to_convert = "lb"
        else:
            print("Error: Invalid unit encountered.")
            break
    print("\nSimulation finished.")