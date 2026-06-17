import math
MASS_TO_KG = 0.000000224146
KG_TO_LBS = 2.2046226218
KG_TO_G = 1000
KG_TO_MG = 1000
KG_TO_TROY_OZ = 31.1034768
def convert_mass(mass_str, target_unit):
    mass = float(mass_str)
    target_unit = target_unit.upper()
    if target_unit == "KG":
        return mass
    elif target_unit == "LBS":
        return mass * KG_TO_LBS
    elif target_unit == "G":
        return mass * KG_TO_G
    elif target_unit == "MG":
        return mass * KG_TO_MG
    elif target_unit == "TROY OZ":
        return mass * KG_TO_TROY_OZ
    else:
        raise ValueError(f"Unsupported target unit: {target_unit}")
if __name__ == '__main__':
    mass_value = "10"
    target_unit = "LBS"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} {target_unit} is {result:.4f}")
    mass_value = "5000"
    target_unit = "KG"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} {target_unit} is {result:.6f}")
    mass_value = "1000"
    target_unit = "G"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} {target_unit} is {result:.4f}")
    mass_value = "1"
    target_unit = "TROY OZ"
    result = convert_mass(mass_value, target_unit)
    print(f"{mass_value} {target_unit} is {result:.6f}")