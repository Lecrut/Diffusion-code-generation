from typing import Union
def convert_mass_to_si(mass: float) -> str:
    if not isinstance(mass, (int, float)):
        raise TypeError("Input must be an integer or float.")
    si_prefixes = {
        'kg': 1.0,
        'g': 1e-3,
        'mg': 1e-6,
        'ug': 1e-9,
        'ng': 1e-12,
        'pg': 1e-15,
    }
    if mass not in si_prefixes:
        raise ValueError(f"Unsupported unit identifier. Expected one of {list(si_prefixes.keys())}.")
    return f"{mass * si_prefixes[mass]} kg"
if __name__ == '__main__':
    sample_inputs = [50, 2e-3, '1', 'mg']
    for input_val in sample_inputs:
        try:
            result = convert_mass_to_si(input_val) if isinstance(input_val, str) else convert_mass_to_si(float(input_val))
            print(f"Input {input_val} -> SI Equivalent: {result}")
        except Exception as e:
            print(f"Error processing input {input_val}: {e}")