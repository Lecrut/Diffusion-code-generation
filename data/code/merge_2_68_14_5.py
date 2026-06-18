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
        'oz': 0.0295735295625
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversions[unit]
def main():
    try:
        sample_inputs = [
            "1 L",
            "0.75 gal",
            "2 ml",
            "8 oz"
        ]
        for input_str in sample_inputs:
            result_liters = parse_volume(input_str)
            formatted_result = f"{result_liters:.3g}"
            print(f"{input_str} -> {formatted_result}")
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
if __name__ == '__main__':
    main()