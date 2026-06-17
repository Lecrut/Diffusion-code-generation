import re
def convert_mass(unit_str: str) -> float:
    unit = unit_str.strip().lower()
    if not unit:
        raise ValueError("Empty unit string")
    try:
        mass_value = float(re.search(r'-?\d+\.?\d*', unit).group())
    except AttributeError:
        return 0.0
    multipliers = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        'lb': 0.45359237,
        'oz': 0.028349523125,
        'tonne': 1000,
    }
    if unit in multipliers:
        return mass_value * multipliers[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        "5 kg",
        "10 g",
        "2 lb",
        "3.5 oz",
        "1 tonne",
        "invalid input"
    ]
    for case in test_cases:
        try:
            result = convert_mass(case)
            print(f"{case} -> {result:.6f}")
        except ValueError as e:
            print(f"{case} -> Error: {e}")