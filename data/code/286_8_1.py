class UnitConversionError(ValueError):
    pass
def convert_length(value: float, unit: str) -> float:
    unit = unit.lower().strip()
    if unit == "m":
        return value
    elif unit == "cm":
        return value / 100.0
    elif unit == "km":
        return value * 1000.0
    elif unit == "in":
        return value * 2.54
    elif unit == "ft":
        return value * 0.3048
    else:
        raise UnitConversionError(f"Invalid unit provided: {unit}. Supported units are 'm', 'cm', 'km', 'in', 'ft'.")
if __name__ == '__main__':
    test_cases = [
        (10.0, "m", 10.0),
        (50.0, "cm", 0.5),
        (2.5, "km", 2500.0),
        (10.0, "in", 25.4),
        (10.0, "ft", 3.048),
    ]
    print("--- Successful Conversions ---")
    for value, unit, expected in test_cases:
        try:
            result = convert_length(value, unit)
            assert abs(result - expected) < 1e-9, f"Test failed for {value} {unit}. Expected {expected}, got {result}"
            print(f"Input: {value} {unit} -> Result: {result} (Expected: {expected}) - PASS")
        except UnitConversionError as e:
            print(f"Input: {value} {unit} -> ERROR: {e} - FAIL")
        except Exception as e:
            print(f"Input: {value} {unit} -> UNEXPECTED ERROR: {e} - FAIL")
    print("\n--- Error Handling Tests ---")
    error_cases = [
        (10.0, "mi"),
        (5.0, "meters "),
        (1.0, "inchs")
    ]
    for value, unit in error_cases:
        try:
            convert_length(value, unit)
            print(f"Input: {value} {unit} -> FAILED (Should have raised an error)")
        except UnitConversionError as e:
            print(f"Input: {value} {unit} -> Caught expected error: {e} - PASS")
        except Exception as e:
            print(f"Input: {value} {unit} -> Caught unexpected error: {e} - FAIL")