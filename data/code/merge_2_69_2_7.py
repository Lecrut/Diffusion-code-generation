import math
CONVERSION_CONSTANTS = {
    "kg": 1,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,
    "oz": 0.02834952,
}
def calculate_mass_scale(from_unit: str, to_unit: str) -> float:
    if from_unit not in CONVERSION_CONSTANTS or to_unit not in CONVERSION_CONSTANTS:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    factor_from_kg = CONVERSION_CONSTANTS[from_unit]
    factor_to_kg = CONVERSION_CONSTANTS[to_unit]
    return abs(factor_from_kg / factor_to_kg)
if __name__ == '__main__':
    sample_result = calculate_mass_scale("lb", "kg")
    print(sample_result)