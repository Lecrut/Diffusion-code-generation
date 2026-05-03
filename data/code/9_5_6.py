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
        "cubic meter": 1000.0
    }
    unit_lower = unit.lower().strip()
    if unit_lower in conversion_factors:
        return volume * conversion_factors[unit_lower]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    test_cases = [
        (1.0, "L"),
        (2.5, "liter"),
        (1000.0, "mL"),
        (500.0, "cm3"),
        (0.001, "cc"),
        (1.0, "m3"),
        (1000.0, "cubic meter"),
        (10.0, "unknown_unit")
    ]
    for volume, unit in test_cases:
        try:
            result = convert_to_liters(volume, unit)
            print(f"Volume: {volume} {unit} -> Liters: {result}")
        except ValueError as e:
            print(f"Error for Volume: {volume}, Unit: {unit}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for Volume: {volume}, Unit: {unit}: {e}")