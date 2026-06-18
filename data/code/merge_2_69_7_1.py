import re
def convert_mass(value_str):
    match = re.match(r'^(\d+\.?\d*)\s*(g|kg)$', value_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid input format")
    num, unit = float(match.group(1)), match.group(2).lower()
    return num * 0.001 if unit == 'g' else num
if __name__ == '__main__':
    test_cases = ["5 g", "1 kg", "250 mg"]
    for case in test_cases:
        try:
            result = convert_mass(case)
            print(f"{case} -> {result:.6f}")
        except ValueError as e:
            print(e)