def compare_strings(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case sensitivity.
    
    Parameters:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        bool: True if the strings match case-insensitively, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("Hello", "HELLO"),           # Should be True
        ("World!", "world!"),         # Should be True
        ("Test123", "TEST456"),       # Should be False (different content)
        ("", ""),                     # Should be True (empty strings match)
        ("CaseInsensitive", "caseinsensitive"),  # Should be True
    ]

    for i, (s1, s2) in enumerate(test_cases, start=1):
        result = compare_strings(s1, s2)
        print(f"Test Case {i}: '{s1}' vs '{s2}' => {result}")