def get_first_letter(s: str) -> str:
    """Returns the first letter of the string if it is non-empty, otherwise returns an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "",
        "a",
        "12345",
        "!@#",
        None, # This will cause an error as expected for invalid input types not handled by the function signature strictly
    ]

    results = []
    for test in test_cases:
        try:
            if isinstance(test, str):
                result = get_first_letter(test)
                print(f"Input: {repr(test)} -> Output: {repr(result)}")
            else:
                # Handling non-string inputs gracefully by converting or skipping based on strictness. 
                # The task asks for a single string input function, but the sample block tests edge cases.
                results.append("Non-string input skipped in main demo.")
        except Exception as e:
            print(f"Error processing {repr(test)}: {e}")

    # Explicit test with None to show behavior if passed directly (though type hint suggests str)
    try:
        res = get_first_letter(None)
        results.append(res)
    except TypeError:
        pass