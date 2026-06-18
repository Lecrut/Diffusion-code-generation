def compare_strings(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case sensitivity.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings match case-insensitively, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_strings("Hello", "HELLO")
    print(f"Test 1 ('Hello', 'HELLO'): {result_1}")

    result_2 = compare_strings("Python", "python3.9")
    print(f"Test 2 ('Python', 'python3.9'): {result_2}")

    result_3 = compare_strings("Different", "different")
    print(f"Test 3 ('Different', 'different'): {result_3}")

    # Ensure the function is working as expected by printing final status
    if result_1 and not result_3:
        print("\nAll tests passed correctly.")
    else:
        print("\nSome tests failed unexpectedly.")