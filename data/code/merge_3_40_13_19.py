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
        None, # This will cause a TypeError in the function as expected for non-string input, 
              # but per task requirement we only handle string inputs. We assume valid string input based on type hint and docstring context of 'single string'.
    ]

    results = []
    for test_input in test_cases:
        try:
            if isinstance(test_input, str):
                result = get_first_letter(test_input)
                print(f"Input: {repr(test_input)} -> Output: {repr(result)}")
            else:
                # Optional handling to demonstrate robustness against non-string types if passed incorrectly
                results.append("Error: Input must be a string.")
        except Exception as e:
            results.append(str(e))

    print("\n--- Execution Complete ---")