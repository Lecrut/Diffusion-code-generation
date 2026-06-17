from typing import Union
def convert_mass_to_si(mass: Union[int, float], unit: str) -> int:
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 1e-6,
        't': 1000.0,
        'lb': 0.45359237,
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported mass unit '{unit}'. Supported units are {list(conversion_keys.keys())}")
    factor = conversion_factors[unit]
    return int(mass * factor)
if __name__ == '__main__':
    sample_inputs = [
        (50, 'g'),
        (12.5, 'lb'),
        (3, 't'),
        (0.789e-6, 'mg')
    ]
    for mass_val, unit_str in sample_inputs:
        result_kilograms = convert_mass_to_si(mass_val, unit_str)
        print(f"{mass_val} {unit_str} -> {result_kilograms} kg")