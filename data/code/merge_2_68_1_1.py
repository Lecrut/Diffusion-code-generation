import re
def convert_to_liters(volume_str: str) -> float:
    volume_str = volume_str.strip().lower()
    unit_match = re.search(r'(\d+\.?\d*)\s*(l|litre|liter|milliliter?|ml|mL|Ml)', volume_str, re.IGNORECASE)
    if not unit_match:
        raise ValueError("Invalid input format. Expected a number followed by 'L', 'l', 'mL', or similar.")
    value = float(unit_match.group(1))
    unit = unit_match.group(2).lower()
    conversion_factors = {
        "liter": 1,
        "litre": 1,
        "ml": 0.001,
        "mL": 0.001,
        "milliliter": 0.001,
        "l": 1,
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported volume unit '{unit}'. Supported units are L, l, mL, ml.")
    return value * conversion_factors[unit]
if __name__ == '__main__':
    test_cases = [
        "5 liters",
        "10.5 milliliters",
        "200ml",
        "3.7 L"
    ]
    for case in test_cases:
        try:
            result = convert_to_liters(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"Error processing '{case}': {e}")