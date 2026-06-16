def safe_to_uppercase(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    else:
        raise TypeError("Input must be a string")
if __name__ == '__main__':
    test_strings = ["hello", "world", "PYTHON", "", "123"]
    test_non_strings = [123, None, 3.14, [], {}]
    print("--- Testing valid strings ---")
    for s in test_strings:
        try:
            result = safe_to_uppercase(s)
            print(f"Input: '{s}' -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: '{s}' -> Error: {e}")
    print("\n--- Testing non-string inputs (expecting errors) ---")
    for n in test_non_strings:
        try:
            result = safe_to_uppercase(n)
            print(f"Input: {n} -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: {n} -> Successfully caught error: {e}")