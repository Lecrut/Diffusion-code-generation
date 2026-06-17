class UnitConversionError(ValueError):
    pass
def convert_length(value: float, unit: str) -> float:
    unit = unit.lower().strip()
    if unit == "m":
        return value
    elif unit == "cm":
        return value * 0.01
    elif unit == "km":
        return value * 1000.0
    elif unit == "in":
        return value * 0.0254
    elif unit == "ft":
        return value * 0.3048
    else:
        raise UnitConversionError(f"Invalid unit provided: {unit}. Supported units are 'm', 'cm', 'km', 'in', 'ft'.")
if __name__ == '__main__':
    test_cases = [
        (10.0, "m", 10.0),
        (50.0, "cm", 500.0),
        (2.5, "km", 2500.0),
        (100.0, "in", 31.48),
        (10.0, "ft", 3.048),
    ]
    print("--- Successful Conversions ---")
    for value, unit, expected in test_cases:
        try:
            result = convert_length(value, unit)
            assert abs(result - expected) < 1e-9, f"Test failed for {value} {unit}. Expected {expected}, got {result}"
            print(f"Input: {value} {unit} -> Result: {result} (PASS)")
        except UnitConversionError as e:
            print(f"Error during successful test case: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
    print("\n--- Error Handling Tests ---")
    error_tests = [
        (10.0, "mi"),
        (5.0, "meters "),
        (20.0, "inch"),
    ]
    for value, unit in error_tests:
        try:
            convert_length(value, unit)
            print(f"FAIL: Expected UnitConversionError for {value} {unit}, but conversion succeeded.")
        except UnitConversionError as e:
            print(f"SUCCESS: Caught expected error for input {value} {unit}: {e}")
        except Exception as e:
            print(f"FAIL: Caught unexpected exception type for input {value} {unit}: {type(e).__name__}")