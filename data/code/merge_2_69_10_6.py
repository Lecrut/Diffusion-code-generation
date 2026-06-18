from typing import Union
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    unit_multipliers = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }
    if from_unit not in unit_multipliers or to_unit not in unit_multipliers:
        raise ValueError(f"Invalid units provided. Supported units: {list(unit_multipliers.keys())}")
    base_value = value * unit_multipliers[from_unit]
    return base_value / unit_multipliers[to_unit]
if __name__ == '__main__':
    test_cases = [
        (10, 'kg', 'g'),
        (5.2, 'lb', 'oz'),
        (1e-3, 'mg', 'g'),
        (0, 'kg', 'lb'),
        (-5, 'kg', 'g')                                 
    ]
    for val, u_from, u_to in test_cases:
        try:
            result = convert_mass(val, u_from, u_to)
            print(f"{val} {u_from} -> {result:.6f} {u_to}")
        except ValueError as e:
            print(f"Error for input ({val}, '{u_from}', '{u_to}')")