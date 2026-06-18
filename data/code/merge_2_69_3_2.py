import math
def convert_grams_to_pounds(grams: float) -> float:
    if grams < 0:
        raise ValueError("Grams must be non-negative.")
    return grams / 453.59237
def convert_kilograms_to_ounces(kg: float) -> float:
    if kg < 0:
        raise ValueError("Kilograms must be non-negative.")
    return kg * 1000 * 28.3495 / 16
def validate_mass_input(value: float, unit_type: str) -> None:
    supported_units = ['grams', 'kilograms']
    if value < 0:
        raise ValueError(f"{unit_type} must be non-negative.")
    if unit_type not in supported_units:
        raise ValueError(f"Unsupported unit type. Supported: {supported_units}")
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    validate_mass_input(value, from_unit)
    conversion_factors = {
        'grams_to_pounds': 1 / 453.59237,
        'kilograms_to_ounces': 1000 * 28.3495 / 16,
        'pounds_to_kilograms': 453.59237 / 1000,
        'ounces_to_grams': 16 / (28.3495)
    }
    factor = conversion_factors.get(f"{from_unit}_{to_unit}")
    if not factor:
        raise ValueError("Conversion pair not supported.")
    return value * factor
if __name__ == '__main__':
    sample_grams = 2036.85
    pounds_result = convert_grams_to_pounds(sample_grams)
    print(f"{sample_grams} grams is {pounds_result:.4f} pounds.")
    kg_sample = 1.5
    ounces_result = convert_kilograms_to_ounces(kg_sample)
    print(f"{kg_sample} kilograms is {ounces_result:.2f} ounces.")
    try:
        invalid_input = -50
        validate_mass_input(invalid_input, 'grams')
    except ValueError as e:
        print(f"Validation error for negative input: {e}")