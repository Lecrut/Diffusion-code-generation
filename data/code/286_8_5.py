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
        (50.0, "cm", 50.0 / 100.0),
        (2.5, "km", 2.5 * 1000.0),
        (100.0, "in", 100.0 * 2.54),
        (10.0, "ft", 10.0 * 0.3048),
    ]
    print("--- Successful Conversions ---")
    for value, unit, expected in test_cases:
        try:
            result = convert_length(value, unit)
            assert abs(result - expected) < 1e-9, f"Test failed for {value} {unit}. Expected {expected}, got {result}"
            print(f"Input: {value} {unit} -> Result: {result} (Expected: {expected}) - PASS")
        except UnitConversionError as e:
            print(f"Error during successful test case: {e} - FAIL")
        except AssertionError as e:
            print(f"Assertion Error: {e} - FAIL")
    print("\n--- Error Handling Tests ---")
    error_cases = [
        (10.0, "mi"),
        (5.0, "meters "),
        (20.0, "inch"),
    ]
    for value, unit in error_cases:
        try:
            convert_length(value, unit)
            print(f"Error Test Failed for {value} {unit}: Expected an error but succeeded.")
        except UnitConversionError as e:
            print(f"Successfully caught expected error for {value} {unit}: {e} - PASS")
        except Exception as e:
            print(f"Caught unexpected exception for {value} {unit}: {type(e).__name__} - FAIL")