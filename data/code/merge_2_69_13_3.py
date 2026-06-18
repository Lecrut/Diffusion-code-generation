CONVERSIONS = {
    'kg_to_lb': 2.20462,
    'g_to_oz': 0.035274
}
def convert_mass(mass: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "kg" and unit_to == "lb":
        return mass * CONVERSIONS['kg_to_lb']
    elif unit_from == "g" and unit_to == "oz":
        return mass * CONVERSIONS['g_to_oz']
if __name__ == '__main__':
    sample_mass_kg = 10.5
    sample_g = 250
    result_lb = convert_mass(sample_mass_kg, 'kg', 'lb')
    print(f"{sample_mass_kg} kg is {result_lb:.4f} lb")
    result_oz = convert_mass(sample_g, 'g', 'oz')
    print(f"{sample_g} g is {result_oz:.4f} oz")