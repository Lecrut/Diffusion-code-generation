import re
def convert_to_liters(volume_str: str) -> float:
    volume_str = volume_str.strip().lower()
    if not volume_str:
        raise ValueError("Empty input")
    match_unit = re.match(r'^([\d.]+)\s*(ml|milliliters?|l|liters?)$', volume_str, re.IGNORECASE)
    if not match_unit:
        try:
            return float(volume_str) * 1000
        except ValueError:
            raise ValueError(f"Invalid input format: {volume_str}")
    value = float(match_unit.group(1))
    unit = match_unit.group(2).lower()
    if 'ml' in unit or 'milliliter' in unit:
        return value / 0.001
    elif 'l' in unit and not any(x in unit for x in ['liter', 'liters']):
        return float(value) * 1000
if __name__ == '__main__':
    test_cases = ["5 ml", "2 liters", "3.5 milliliters", "1 l"]
    results = []
    for case in test_cases:
        try:
            result = convert_to_liters(case)
            results.append(result)
        except Exception as e:
            print(f"Error with {case}: {e}")
    if len(results) > 0:
        print("Converted values:", results[0], results[1], results[2], results[3])