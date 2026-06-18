def strings_equal(case_insensitive=True):
    """
    Checks if two input strings are equal with optional case-insensitivity.
    
    Args:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.
        
    Returns:
        bool: True if the strings are equal, False otherwise.
    """
    try:
        return str(s1).lower() == str(s2).lower()
    except TypeError:
        raise ValueError("Both arguments must be convertible to strings.")

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    result1 = strings_equal('Hello', 'hello')  # Expected True
    print(f"'Hello' vs 'hello': {result1}")  
    
    result2 = strings_equal('World!', 'WORLD!')  # Expected True
    print(f"'World!' vs 'WORLD!': {result2}") 
    
    result3 = strings_equal('', '')  # Expected True (empty string)
    print(f"'' vs '': {result3}")  
    
    result4 = strings_equal('Different', 'different')  # Expected False due to length difference? Actually this is tricky. Let's fix the logic:
    
    # Correction for the above test case, they should be equal if lengths are same and characters match ignoring case
    print(f"'Different' vs 'different': {strings_equal('Different', 'different')}") 
    
    result5 = strings_equal(123, 456)  # Expected False (integers converted to string "123" != "456")
    print(f'"123" vs "456": {result5}')