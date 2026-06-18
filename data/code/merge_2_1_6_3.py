def is_binary_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return all(c in '01' for c in s)
if __name__ == '__main__':
    test_cases = [
        "101",
        "000",
        "abc",
        123,
        None,
        "",
        "1a"
    ]
    for case in test_cases:
        try:
            result = is_binary_string(case)
            print(f"'{case}': {result}")
        except TypeError as e:
            print(f"{type(case).__name__}: Error - {e}")