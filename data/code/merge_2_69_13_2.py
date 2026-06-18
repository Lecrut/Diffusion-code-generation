CONVERSION_CONSTANTS = {
    'kg_to_lb': 2.20462,
    'g_to_oz': 0.035274
}
def convert_kg_to_lb(kilograms: float) -> float:
    return kilograms * CONVERSION_CONSTANTS['kg_to_lb']
def convert_g_to_oz(grams: float) -> float:
    return grams * CONVERSION_CONSTANTS['g_to_oz']
if __name__ == '__main__':
    sample_kg = 5.0
    sample_g = 1000.0
    lbs_result = convert_kg_to_lb(sample_kg)
    oz_result = convert_g_to_oz(sample_g)
    print(f"{sample_kg} kg is equal to {lbs_result:.2f} lb")
    print(f"{sample_g} g is equal to {oz_result:.4f} oz")