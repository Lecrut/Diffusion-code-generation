import sys
def convert_mass(value_str):
    try:
        value = float(value_str)
    except ValueError:
        return None
    unit_map = {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6,
        "tonne": 1000,
        "lb": 0.45359237,
    }
    if value_str not in unit_map:
        return None
    factor = unit_map[value_str]
    return round(value * factor, 6)
if __name__ == '__main__':
    test_cases = ["10", "2.5g", "3mg", "4tonne", "5lb"]
    for case in test_cases:
        result = convert_mass(case)
        if result is not None:
            print(result, "kg")