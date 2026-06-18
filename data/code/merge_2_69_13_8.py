CONVERSION_CONSTANTS = {
    "kg_to_lb": 2.20462,
    "g_to_oz": 0.035274
}
def convert_mass(mass: float, unit_from: str, unit_to: str) -> float:
    if not isinstance(unit_from, str):
        raise ValueError("Unit from must be a string.")
    factor = CONVERSION_CONSTANTS.get(f"{unit_from}_to_{unit_to}", None)
    return mass * factor
if __name__ == '__main__':
    sample_kg = 5.0
    result_lb = convert_mass(sample_kg, "kg", "lb")
    sample_g = 1000.0
    result_oz = convert_mass(sample_g, "g", "oz")
    print(f"{sample_kg} kg is {result_lb:.4f} lb.")
    print(f"{sample_g} g is {result_oz:.4f} oz.")