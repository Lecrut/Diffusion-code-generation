import math
def convert_to_liters(volume: float, unit: str) -> float:
    conversion_factors = {
        "L": 1.0,
        "liter": 1.0,
        "liters": 1.0,
        "mL": 0.001,
        "ml": 0.001,
        "cm3": 0.000001,
        "cc": 0.001,
        "m3": 1000.0,
        "cubic meter": 1000.0,
        "m3": 1000.0,
        "ft3": 28.316846592,
        "cubic foot": 28.316846592,
        "gal": 3.785411784,
        "gallon": 3.785411784,
        "qt": 0.946352946,
        "quart": 0.946352946,
        "fl oz": 0.0295735295625,
        "fluid ounce": 0.0295735295625,
        "in3": 0.016387064,
        "cubic inch": 0.016387064,
    }
    unit_lower = unit.lower().strip()
    if unit_lower in conversion_factors:
        factor = conversion_factors[unit_lower]
        return volume * factor
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        (1.0, "L"),
        (10.0, "mL"),
        (1.0, "cm3"),
        (1.0, "m3"),
        (1.0, "gallon"),
        (100.0, "ft3"),
        (1.0, "liter"),
        (1.0, "cubic meter"),
    ]
    for volume, unit in test_cases:
        try:
            result = convert_to_liters(volume, unit)
            print(f"Volume: {volume} {unit} -> {result:.10f} L")
        except ValueError as e:
            print(f"Error for {volume} {unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {volume} {unit}: {e}")