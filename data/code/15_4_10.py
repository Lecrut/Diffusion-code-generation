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
    # Sample test cases running without user input or external dependencies
    
    result1 = compare_strings("Hello", "hello")
    print(f"Test 1 ('Hello' vs 'hello'): {result1}")  # Expected: True
    
    result2 = compare_strings("Python", "java")
    print(f"Test 2 ('Python' vs 'java'): {result2}")  # Expected: False
    
    result3 = compare_strings("", "")
    print(f"Test 3 ('' vs ''): {result3}")  # Expected: True