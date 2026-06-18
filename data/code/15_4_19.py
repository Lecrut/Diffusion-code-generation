def compare_strings(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case sensitivity.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings match when compared in a case-insensitive manner, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    test_cases = [
        ("Hello", "hello"),
        ("HELLO WORLD!", "World!"),
        ("Python 3.10", "python 3.10"),
        ("Different Strings", "different strings"),
        ("Case Insensitive Test", "case insensitive TEST"),
    ]

    for idx, (s1, s2) in enumerate(test_cases):
        result = compare_strings(s1, s2)
        print(f"Test {idx + 1}: '{s1}' vs '{s2}' -> {'Match' if result else 'No Match'}")