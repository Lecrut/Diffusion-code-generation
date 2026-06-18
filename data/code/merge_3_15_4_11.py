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
    # Sample test cases run without user input or external dependencies
    
    assert compare_strings("Hello", "hello") is True
    assert compare_strings("Python 3.9", "PYTHON 3.9") is True
    assert compare_strings("Test123", "test456") is False
    assert compare_strings("", "") is True
    print("All assertions passed.")