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
        raise ValueError(f"Unsupported unit '{mass_input}'. Supported units are {list(conversion_factors.keys())}.")
    return float(mass_input) * conversion_factors[mass_input.lower()]
if __name__ == '__main__':
    test_cases = [
        "5 kg",
        "10 g",
        "2 mg",
        "3 tonne",
        "4 lb"
    ]
    for case in test_cases:
        try:
            result = convert_mass_to_si(case)
            print(f"{case} -> {result:.6f} kg")
        except ValueError as e:
            print(e)