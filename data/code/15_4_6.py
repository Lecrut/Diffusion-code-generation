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
    
    result_1 = compare_strings("Hello", "hello")
    print(f"'Hello' vs 'hello': {result_1}")  # Expected: True
    
    result_2 = compare_strings("World!", "WORLD!")
    print(f"'World!' vs 'WORLD!': {result_2}")  # Expected: True
    
    result_3 = compare_strings("Python", "Java")
    print(f"'Python' vs 'Java': {result_3}")   # Expected: False