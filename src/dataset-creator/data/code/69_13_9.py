CONVERSION_CONSTANTS = {
    'kg_to_lb': 2.20462,
    'g_to_oz': 0.035274
}
def convert_mass(mass: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "kilograms" and unit_to == "pounds":
        return mass * CONVERSION_CONSTANTS['kg_to_lb']
    elif unit_from == "grams" and unit_to == "ounces":
        return mass * CONVERSION_CONSTANTS['g_to_oz']
    else:
        raise ValueError("Unsupported conversion pair")
if __name__ == '__main__':
    sample_mass_kg = 10.5
    sample_grammage = 250
    result_lb = convert_mass(sample_mass_kg, "kilograms", "pounds")
    print(f"{sample_mass_kg} kilograms is {result_lb:.4f} pounds.")
    result_oz = convert_mass(sample_grammage, "grams", "ounces")
    print(f"{sample_grammage} grams is {result_oz:.4f} ounces.")