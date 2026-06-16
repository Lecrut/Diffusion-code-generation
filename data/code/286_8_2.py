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
        raise ValueError(f"Invalid unit provided: {unit}. Supported units are 'm', 'cm', 'km', 'in', 'ft'.")
if __name__ == '__main__':
    test_cases = [
        (10.0, "m", 10.0),
        (50.0, "cm", 0.5),
        (2.5, "km", 2500.0),
        (12.0, "in", 30.48),
        (10.0, "ft", 3.048),
    ]
    print("--- Testing Valid Conversions ---")
    for value, unit, expected in test_cases:
        try:
            result = convert_length(value, unit)
            assert abs(result - expected) < 1e-9, f"Input: {value} {unit}, Expected: {expected}, Got: {result}"
            print(f"PASS: {value} {unit} -> {result}")
        except ValueError as e:
            print(f"FAIL (Unexpected Error): {value} {unit}. Error: {e}")
        except AssertionError as e:
            print(f"FAIL (Assertion Error): {e}")
    print("\n--- Testing Invalid Unit Handling ---")
    invalid_tests = [
        (10.0, "mi"),
        (5.0, "meters"),
        (1.0, "X"),
    ]
    for value, unit in invalid_tests:
        try:
            convert_length(value, unit)
            print(f"FAIL (Unexpected Success): {value} {unit} succeeded unexpectedly.")
        except ValueError as e:
            print(f"PASS (Caught Error): Attempted conversion of {value} {unit}. Caught expected error: {e}")