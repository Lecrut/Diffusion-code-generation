import re
def parse_volume(input_str):
    pattern = r'^(\d+\.?\d*)\s*(L|l|ml|mL|gal|gallons?|oz|ounces?)$'
    match = re.match(pattern, input_str.strip())
    if not match:
        raise ValueError("Invalid volume format")
    value = float(match.group(1))
    unit = match.group(2).lower()
    conversions = {
        'l': 1.0,
        'ml': 0.001,
        'gal': 3.785411784,
        'ounces': 0.0295735295625
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversions[unit]
if __name__ == '__main__':
    try:
        test_cases = [
            "10 L",
            "5 ml",
            "2 gal",
            "3.5 oz"
        ]
        for case in test_cases:
            result_liters = parse_volume(case)
            formatted_result = f"{result_liters:.3g}"
            print(formatted_result, "L")
    except ValueError as e:
        print(f"Error: {e}")