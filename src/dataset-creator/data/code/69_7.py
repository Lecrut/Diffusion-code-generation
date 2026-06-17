import re
def convert_mass(value: str) -> float:
    pattern = r'^(\d+\.?\d*)\s*(g|kg|mg|t)?$'
    match = re.match(pattern, value.strip())
    if not match:
        raise ValueError("Invalid input format. Expected number followed by optional unit (g/kg/mg/t).")
    num = float(match.group(1))
    unit = match.group(2) or 'kg'                 
    multipliers = {
        'g': 0.001,
        'kg': 1.0,
        'mg': 0.000001,
        't': 1000.0
    }
    return num * multipliers.get(unit.lower(), None)
if __name__ == '__main__':
    test_cases = [
        "5 g",
        "2 kg",
        "3 mg",
        "4 t"
    ]
    for case in test_cases:
        try:
            result = convert_mass(case)
            print(f"{case} -> {result:.6f}")
        except ValueError as e:
            print(e)