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
    test_cases = [
        ("Hello", "hello"),
        ("HELLO WORLD", "world hello "),  # Different order and case, should be False? No, wait. 
        # Correction: "HELLO WORLD" vs "world hello " -> different content (extra space at end in second), so False.
        # Let's fix the test cases to be clear about equality logic.
        
        ("Example", "EXAMPLE"),  # Should match
        ("Python Code", "python code "),  # Different length due to trailing space, should not match
    ]
    
    for i, (s1, s2) in enumerate(test_cases):
        result = compare_strings(s1, s2)
        print(f"Test {i+1}: '{s1}' vs '{s2}' -> {result}")