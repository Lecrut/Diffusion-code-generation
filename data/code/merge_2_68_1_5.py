import re
def convert_to_liters(volume_str: str) -> float:
    volume_str = volume_str.strip().lower()
    conversions = {
        'liter': 1.0,
        'litre': 1.0,
        'l': 1.0,
        'ml': 0.001,
        'milliliter': 0.001,
        'mL': 0.001,
        'gal': 3.785411784,
        'gallon': 3.785411784,
        'us gal': 3.785411784,
        'fl oz': 0.0295735295625,
        'fluid ounce': 0.0295735295625,
        'oz': 0.0295735295625,
        'qt': 0.946352946,
        'quart': 0.946352946,
        'pt': 0.473176473,
        'pint': 0.473176473,
    }
    match = re.match(r'^([\d.]+)\s*(\w+)$', volume_str)
    if not match:
        raise ValueError(f"Invalid input format: {volume_str}")
    try:
        number = float(match.group(1))
    except ValueError:
        raise ValueError("Numeric value must be a valid decimal number")
    unit = match.group(2).strip()
    if unit not in conversions:
        raise ValueError(f"Unsupported volume unit: {unit}")
    return number * conversions[unit]
if __name__ == '__main__':
    test_cases = [
        "5 liters",
        "10 ml",
        "2.5 gal",
        "3 fl oz",
        "half a liter"                                                                                                                                                                                                                                                                                                                                                                                    
    ]
    samples = [
        "10 ml",
        "2.5 gal",
        "3 fl oz",
        "7 qt"
    ]
    for sample in samples:
        try:
            result = convert_to_liters(sample)
            print(f"{sample} -> {result}")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")