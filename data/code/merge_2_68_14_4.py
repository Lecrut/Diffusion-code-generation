import re
from typing import Optional
def parse_volume(input_str: str) -> float | None:
    pattern = r'^\s*([+-]?\d+(?:[.,]\d+)?)\s*(L|l|ml|mL|gal|oz)\s*$'
    match = re.match(pattern, input_str.strip())
    if not match:
        return None
    try:
        value = float(match.group(1))
        unit = match.group(2).lower()
        conversions = {
            'l': 1.0,
            'ml': 0.001,
            'gal': 3.785411784,
            'oz': 0.0295735296
        }
        if unit not in conversions:
            return None
        liters = value * conversions[unit]
        return round(liters, 3)
    except ValueError:
        return None
if __name__ == '__main__':
    test_cases = [
        "5 L",
        "2.5 ml",
        "10 gal",
        "0.75 oz",
        "-3 L",
        "invalid input",
        "abc 10 l"
    ]
    for case in test_cases:
        result = parse_volume(case)
        if result is None:
            print(f"{case} -> Error")
        else:
            formatted_result = f"{result:.3g}"
            print(f"{case} -> {formatted_result}")