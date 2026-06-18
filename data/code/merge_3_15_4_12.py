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
    # Sample test cases run directly without user input or external dependencies
    
    # Test 1: Identical strings with different casing
    result = compare_strings("Hello", "HELLO")
    
    # Test 2: Different strings that might appear similar ignoring case (intentionally False)
    result_false = compare_strings("World", "Python")
    
    # Test 3: Empty strings equality
    result_empty = compare_strings("", "")
    
    print(f"Test 1 ('Hello', 'HELLO') -> {result}")   # Expected True
    print(f"Test 2 ('World', 'Python') -> {result_false}") # Expected False
    print(f"Test 3 ('' vs '') -> {result_empty}")         # Expected True