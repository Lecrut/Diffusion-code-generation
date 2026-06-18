import re
def parse_volume(input_str):
    pattern = r'^([\d.]+)\s*(L|ml|gal|oz)$'
    match = re.match(pattern, input_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError("Invalid volume format")
    try:
        value = float(match.group(1))
    except ValueError:
        raise ValueError("Numeric conversion failed")
    unit = match.group(2).lower()
    conversions = {
        'l': 1.0,
        'ml': 0.001,
        'gal': 3.785411784,
        'oz': 0.0295735295625
    }
    return value * conversions.get(unit)
def main():
    test_cases = [
        "5 L",
        "100 ml",
        "2 gal",
        "8 oz"
    ]
    for case in test_cases:
        try:
            liters = parse_volume(case)
            formatted_result = f"{liters:.3g}"
            print(formatted_result)
        except ValueError as e:
            print(f"Error processing '{case}': {e}")
if __name__ == '__main__':
    main()