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
    print(f"Test 1 ('Hello' vs 'hello'): {result1}")

    result2 = compare_strings("World!", "WORLD!")
    print(f"Test 2 ('World!' vs 'WORLD!'): {result2}")

    result3 = compare_strings("Python", "java")
    print(f"Test 3 ('Python' vs 'java'): {not result3}")