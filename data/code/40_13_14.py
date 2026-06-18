def get_first_letter(s: str) -> str:
    """Returns the first letter of the string if it exists, otherwise returns an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "",
        "a",
        "!@#",
        None  # This will cause a TypeError, which is expected behavior for invalid input types not specified in the signature.
              # To strictly adhere to 'single string' requirement as per task description:
    ]

    samples = [
        ("Hello World", "H"),
        ("", ""),
        ("a", "a")
    ]

    print("Testing get_first_letter function:")
    for input_str, expected in samples:
        try:
            result = get_first_letter(input_str)
            status = "PASS" if result == expected else f"FAIL (got {result!r})"
            print(f"Input: {input_str!r} -> Output: {result!r} [{status}]")
        except Exception as e:
            # The function signature expects a string. If None is passed, it raises TypeError. 
            # We handle the valid cases from 'samples' list above which only contains strings or empty strings.
            print(f"Input: {input_str!r} -> Error: {e}")

    # Explicit test with hard-coded values as requested in sample block logic without user input
    explicit_tests = [
        ("Python", "P"),
        ("" , ""),
        ("z", "z")
    ]

    print("\nExplicit Hard-Coded Tests:")
    for inp, exp in explicit_tests:
        res = get_first_letter(inp)
        assert res == exp, f"Expected {exp}, got {res}"
        print(f"get_first_letter({inp!r}) returned {res!r} (Correct)")