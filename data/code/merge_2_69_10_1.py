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
    if value == 0:
        return 0
    try:
        base_value = abs(value) * conversion_factors[from_unit.lower()]
        result = -base_value / conversion_factors[to_unit.lower()] if value < 0 else base_value / conversion_factors[to_unit.lower()]
    except ZeroDivisionError:
        raise ValueError("Cannot convert to zero units.")
    return round(result, 6)
if __name__ == '__main__':
    sample_input = {
        'from_unit': 'kg',
        'to_unit': 'g'
    }
    try:
        result = convert_mass(50.5, **sample_input)
        print(f"Converted value from {sample_input['from_unit']} to {sample_input['to_unit']}: {result}")
        test_zero = convert_mass(0, 'kg', 'g')
        assert test_zero == 0
    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")