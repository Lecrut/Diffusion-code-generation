CONVERSION_CONSTANTS = {
    'kg_to_lb': 2.20462,
    'g_to_oz': 0.035274
}
def convert_mass(mass_value: float, unit_from: str, unit_to: str) -> float:
    if unit_from == "kilograms" and unit_to == "pounds":
        return mass_value * CONVERSION_CONSTANTS['kg_to_lb']
    elif unit_from == "grams" and unit_to == "ounces":
        return mass_value * CONVERSION_CONSTANTS['g_to_oz']
    else:
        raise ValueError("Unsupported conversion pair")
if __name__ == '__main__':
    sample_kilograms = 5.0
    sample_grams = 1000.0
    result_lb = convert_mass(sample_kilograms, "kilograms", "pounds")
    print(f"{sample_kilograms} kilograms is {result_lb:.2f} pounds.")
    result_oz = convert_mass(sample_grams, "grams", "ounces")
    print(f"{sample_grams} grams is {result_oz:.4f} ounces.")