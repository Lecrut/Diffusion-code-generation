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
    result1 = compare_strings("Hello", "hello")
    result2 = compare_strings("Python 3.9", "python 3.9")
    result3 = compare_strings("Different", "different!")

    print(f"Test 1 ('Hello', 'hello'): {result1}")   # Expected: True
    print(f"Test 2 ('Python 3.9', 'python 3.9'): {result2}")  # Expected: True
    print(f"Test 3 ('Different', 'different!'): {result3}")  # Expected: False