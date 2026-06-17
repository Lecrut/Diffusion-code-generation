from typing import Union
def convert_mass_to_si(mass: float) -> str:
    if not isinstance(mass, (int, float)):
        raise TypeError("Input must be an integer or float.")
    si_prefixes = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 1e-6,
        "ug": 1e-9,
        "t": 1000.0,
        "Mg": 1_000_000.0,
    }
    if mass not in si_prefixes:
        raise ValueError(f"Unsupported unit identifier '{mass}'.")
    converted_value = mass * si_prefixes[mass]
    return f"{converted_value} kg"
if __name__ == '__main__':
    sample_inputs = [5, 1000, "2", "3.5"]
    for input_val in sample_inputs:
        try:
            result = convert_mass_to_si(input_val)
            print(f"{input_val} -> {result}")
        except Exception as e:
            print(f"Error processing '{input_val}': {e}")