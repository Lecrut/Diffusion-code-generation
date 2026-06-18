from typing import Union
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    valid_units = ['kg', 'g', 'mg']
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
    if from_unit.lower() not in [u.lower() for u in valid_units]:
        raise ValueError(f"Invalid source unit. Must be one of {valid_units}")
    if to_unit.lower() not in [u.lower() for u in valid_units]:
        raise ValueError(f"Invalid target unit. Must be one of {valid_units}")
    conversion_factors = {'kg': 1, 'g': 0.001, 'mg': 0.000001}
    try:
        value_in_kg = value * conversion_factors[from_unit.lower()]
        result_value = value_in_kg / conversion_factors[to_unit.lower()]
        if not isinstance(result_value, float):
            raise TypeError("Conversion failed.")
        return round(result_value, 6)
    except ZeroDivisionError:
        return None
if __name__ == '__main__':
    sample_input = convert_mass(1000, 'g', 'kg')
    if sample_input is not None:
        print(f"Converted value from {sample_input} to kg")