CONVERSION_CONSTANTS = {
    'kg_to_lb': 2.20462,
    'g_to_oz': 0.035274
}
def convert_mass(mass: float, unit_from: str, unit_to: str) -> float:
    if not isinstance(unit_from, str):
        raise ValueError("Unit from must be a string.")
    conversion_factor = CONVERSION_CONSTANTS.get(f"{unit_from}_to_{unit_to}")
    return mass * conversion_factor
if __name__ == '__main__':
    sample_mass_kg = 10.5
    pounds_result = convert_mass(sample_mass_kg, 'kg', 'lb')
    grams_value = 2500.0
    ounces_result = convert_mass(grams_value, 'g', 'oz')
    print(f"{sample_mass_kg} kg is equal to {pounds_result:.4f} lbs.")
    print(f"{grams_value} g is equal to {ounces_result:.4f} oz.")