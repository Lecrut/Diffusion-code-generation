def case_insensitive_equal(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal in a case-insensitive manner.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        bool: True if the strings are equal ignoring case, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ("Hello", "hello"),
        ("HELLO WORLD", "world HELLO"),
        ("Python 3.9", "python 3.9"),
        ("Different Strings", "different strings"),
        ("CaseInsensitiveTest123!", "CASEINSENSITIVETEST123!"),
    ]

    for s1, s2 in sample_cases:
        result = case_insensitive_equal(s1, s2)
        print(f"Comparing '{s1}' and '{s2}': {'Equal' if result else 'Not Equal'}")