from typing import Union
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    unit_factors = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 1e-6,
        "lb": 0.45359237,
        "oz": 0.028349523125
    }
    if value == 0:
        return 0.0
    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise ValueError(f"Invalid units provided. Supported units are {list(unit_factors.keys())}")
    factor_from = unit_factors[from_unit]
    factor_to = unit_factors[to_unit]
    value_in_kg = value * factor_from
    result_value = value_in_kg / factor_to
    return round(result_value, 6)
if __name__ == '__main__':
    sample_input_1 = convert_mass(50.0, "kg", "lb")
    print(f"Sample 1: {sample_input_1}")
    try:
        invalid_result = convert_mass(-10.0, "km", "m")
    except ValueError as e:
        print(f"Error caught for sample 2: {e}")
    zero_test = convert_mass(0, "g", "kg")
    print(f"Sample 3 (Zero input): {zero_test}")