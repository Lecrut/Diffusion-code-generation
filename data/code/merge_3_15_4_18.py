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
    
    # Test 1: Exact same string
    result1 = compare_strings("Hello", "hello")
    
    # Test 2: Different strings with different casing
    result2 = compare_strings("World!", "WORLD!")
    
    # Test 3: Completely different content
    result3 = compare_strings("Python", "Java")
    
    print(f"Test 1 ('Hello' vs 'hello'): {result1}")   # Expected: True
    print(f"Test 2 ('World!' vs 'WORLD!'): {result2}") # Expected: True
    print(f"Test 3 ('Python' vs 'Java'): {result3}")     # Expected: False
    
    assert result1 == True, "Test 1 failed"
    assert result2 == True, "Test 2 failed"
    assert result3 == False, "Test 3 failed"
    
    print("All tests passed.")