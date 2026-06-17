import re
def convert_to_liters(volume_str: str) -> float:
    volume_str = volume_str.strip().lower()
    unit_match = re.search(r'(\d+\.?\d*)\s*(liter|litre|l|ml|mL?|milliliter|m)?', volume_str, re.IGNORECASE)
    if not unit_match:
        raise ValueError("Invalid input format")
    value = float(unit_match.group(1))
    unit = unit_match.group(2).lower()
    conversion_factors = {
        'liter': 1.0,
        'litre': 1.0,
        'l': 1.0,
        'ml': 0.001,
        'mL': 0.001,
        'milliliter': 0.001,
        'm': 0.001
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported volume unit: {unit}")
    return value * conversion_factors[unit]
if __name__ == '__main__':
    test_cases = [
        "5 liters",
        "2.5 litre",
        "10 l",
        "3 ml",
        "7 milliliter",
        "0.5 mL"
    ]
    for case in test_cases:
        result = convert_to_liters(case)
        print(f"{case} -> {result}")