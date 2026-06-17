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
        (100.0, "in", 25.4),
        (10.0, "ft", 3.048),
    ]
    print("--- Length Conversion Tests ---")
    for value, unit, expected in test_cases:
        try:
            result = convert_length(value, unit)
            assert abs(result - expected) < 1e-9, f"Input: {value} {unit}, Expected: {expected}, Got: {result}"
            print(f"PASS: {value} {unit} -> {result}")
        except ValueError as e:
            print(f"FAIL (Unexpected Error): {value} {unit} -> {e}")
        except AssertionError as e:
            print(f"FAIL (Assertion Error): {e}")
    print("\n--- Error Handling Tests ---")
    error_cases = [
        (10.0, "mi"),
        (5.0, "meters "),
        (10.0, "inch"),
    ]
    for value, unit in error_cases:
        try:
            convert_length(value, unit)
            print(f"FAIL (Did not raise error): {value} {unit}")
        except ValueError as e:
            print(f"PASS (Correctly caught error for '{value} {unit}'): {e}")