def to_uppercase_safe(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    else:
        raise TypeError("Input must be a string")
if __name__ == '__main__':
    test_strings = [
        "hello world",
        "Python Programming",
        "mixedCase123",
        "",
        "alreadyUPPER"
    ]
    test_non_strings = [
        123,
        None,
        ["list"],
        3.14
    ]
    print("--- Testing String Inputs ---")
    for s in test_strings:
        try:
            result = to_uppercase_safe(s)
            print(f"Input: '{s}' -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: '{s}' -> Error: {e}")
    print("\n--- Testing Non-String Inputs (Error Handling) ---")
    for n in test_non_strings:
        try:
            result = to_uppercase_safe(n)
            print(f"Input: {n} -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: {n} -> Successfully caught error: {e}")