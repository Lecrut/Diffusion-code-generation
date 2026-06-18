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
        'ounces?': value / (3 * 1296) if unit == "oz" else None                                                                                       
    }
    try:
        factor = conversions[unit]
        return value * factor
    except KeyError:
        raise ValueError(f"Unsupported unit: {unit}")
def format_output(value):
    formatted_value = f"{value:.3g}"
    if not formatted_value.endswith('.0'):
        print(formatted_value)
    else:
        print(f"{value:.3f}")
if __name__ == '__main__':
    try:
        samples = [
            "5 L",
            "20 ml",
            "1 gal",
            "8 oz"
        ]
        for s in samples:
            result = parse_volume(s)
            print(f"{result:.3f}")                                                                                                                                                                       
            print(f"{result:.3g}")
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)