import sys
def convert_mass(mass, unit):
    if unit == "kg":
        if mass == 0:
            return 0.0, "kg"
        elif mass == 1:
            return 1000.0, "g"
        else:
            return mass * 1000.0, "g"
    elif unit == "g":
        if mass == 0:
            return 0.0, "g"
        elif mass == 1000:
            return 1.0, "kg"
        else:
            return mass / 1000.0, "kg"
    elif unit == "lb":
        if mass == 0:
            return 0.0, "lb"
        elif mass == 1:
            return 0.453592, "kg"
        else:
            return mass / 2.20462, "kg"
    else:
        return None, "Unknown unit"
if __name__ == '__main__':
    mass_values = [1000, 500, 1500]
    unit_values = ["kg", "g", "lb"]
    for i in range(len(mass_values)):
        mass = mass_values[i]
        unit = unit_values[i]
        print(f"--- Iteration {i + 1} ---")
        print(f"Starting with Mass: {mass} {unit}")
        if unit == "kg":
            grams, _ = convert_mass(mass, "kg")
            print(f"Conversion to grams: {grams:.2f} g")
        elif unit == "g":
            kilograms, _ = convert_mass(mass, "g")
            print(f"Conversion to kilograms: {kilograms:.3f} kg")
        elif unit == "lb":
            kilograms, _ = convert_mass(mass, "lb")
            print(f"Conversion to kilograms: {kilograms:.3f} kg")
        else:
            print("Invalid unit provided.")
        print("-" * 20)
    print("Program finished.")