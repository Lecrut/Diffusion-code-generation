import re
def parse_volume(input_str):
    pattern = r'^\s*([\d\.]+)\s*(L|l|ml|mL|gal|gallons?|oz|ounces?)\s*$'
    match = re.match(pattern, input_str.strip())
    if not match:
        raise ValueError("Invalid volume format")
    try:
        value = float(match.group(1))
    except ValueError:
        raise ValueError("Numeric conversion failed for the provided amount")
    unit = match.group(2).lower()
    conversions = {
        'l': 1.0,
        'ml': 0.001,
        'gal': 3.78541,
        'oz': 0.0295735
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversions[unit]
if __name__ == '__main__':
    test_cases = [
        "1 L",
        "5 ml",
        "2 gal",
        "0.75 oz",
        "invalid input",
        "abc 3L"
    ]
    for case in test_cases:
        try:
            liters = parse_volume(case)
            print(f"{case} -> {liters:.3g} L")
        except ValueError as e:
            print(f"Error processing '{case}': {e}")