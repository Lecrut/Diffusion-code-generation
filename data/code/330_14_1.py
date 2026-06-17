def to_uppercase_safe(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    else:
        raise TypeError("Input must be a string.")
if __name__ == '__main__':
    test_strings = ["hello", "world", "PYTHON", "", "123"]
    test_non_strings = [123, 3.14, None, [], {}]
    print("Testing valid strings:")
    for s in test_strings:
        try:
            result = to_uppercase_safe(s)
            print(f"Input: '{s}' -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: '{s}' -> Error: {e}")
    print("\nTesting non-string inputs (expecting errors):")
    for n in test_non_strings:
        try:
            result = to_uppercase_safe(n)
            print(f"Input: {n} -> Output: '{result}'")
        except TypeError as e:
            print(f"Input: {n} -> Caught expected error: {e}")