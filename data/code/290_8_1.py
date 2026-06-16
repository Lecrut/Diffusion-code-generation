import math
def convert_mass(mass_str: str, target_unit: str) -> float:
    mass = float(mass_str)
    if target_unit == "kg":
        return mass
    elif target_unit == "g":
        return mass * 1000.0
    elif target_unit == "lb":
        return mass * 2.2046226218
    elif target_unit == "oz":
        return mass * 35.27396195
    else:
        raise ValueError("Unsupported target unit")
if __name__ == '__main__':
    mass_value = "10"
    target_unit = "kg"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} {target_unit} is equal to {result}")
    mass_value = "500"
    target_unit = "g"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} g is equal to {result} kg")
    mass_value = "2.2046226218"
    target_unit = "lb"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} lb is equal to {result} kg")
    mass_value = "16"
    target_unit = "oz"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} oz is equal to {result} kg")