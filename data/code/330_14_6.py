def to_uppercase_safe(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    else:
        raise TypeError("Input must be a string")
if __name__ == '__main__':
    test_strings = [
        "hello world",
        "Python",
        "this is a test",
        "",
        "already UPPER"
    ]
    test_non_strings = [
        123,
        None,
        ["list"],
        3.14
    ]
    print("--- Testing valid strings ---")
    for s in test_strings:
        try:
            result = to_uppercase_safe(s)
            print(f"Input: '{s}' -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: '{s}' -> Error: {e}")
    print("\n--- Testing invalid types (Error Handling) ---")
    for nt in test_non_strings:
        try:
            result = to_uppercase_safe(nt)
            print(f"Input: {nt} -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: {nt} -> Caught expected error: {e}")