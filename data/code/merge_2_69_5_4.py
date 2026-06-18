from typing import Union
def convert_mass_to_si(mass_input: str) -> float:
    conversion_factors = {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6,
        "tonne": 1000,
        "lb": 0.45359237,
    }
    if mass_input.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit '{mass_input}'. Supported units are {list(conversion_factors.keys())}")
    return float(mass_input) * conversion_factors[mass_input.lower()]
if __name__ == '__main__':
    sample_inputs = ["5 kg", "200 g", "1.5 tonne", "3 lb"]
    for input_str in sample_inputs:
        try:
            result = convert_mass_to_si(input_str)
            print(f"{input_str} -> {result:.6f}")
        except ValueError as e:
            print(e)