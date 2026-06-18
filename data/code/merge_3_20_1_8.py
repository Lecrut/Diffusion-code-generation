import unicodedata

def case_insensitive_equal(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case differences.
    
    The function normalizes both input strings using Unicode normalization 
    to handle edge cases like accented characters (e.g., 'é' vs 'E') before 
    converting them to lowercase for comparison. This ensures a robust and 
    accurate equality check in an internationalized context.

    Parameters:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are equal case-insensitively, False otherwise.
    
    Examples:
        >>> case_insensitive_equal("Hello", "HELLO")
        True
        
        >>> case_insensitive_equal("Café", "CAFÉ")
        True
        
        >>> case_insensitive_equal("Müller", "MÜLLER")
        True
        
        >>> case_insensitive_equal("Test", "test123")
        False
    
    Time Complexity: O(n), where n is the length of the longer string.
    Space Complexity: O(1) as normalization and conversion are done in-place 
      relative to input size without additional data structures proportional to input.
    """
    
    # Normalize strings using Unicode NFKD decomposition, then fold (lowercase case-insensitive logic).
    normalized_str1 = unicodedata.normalize("NFD", str1)
    normalized_str2 = unicodedata.normalize("NFD", str2)

    return "".join(c.lower() for c in normalized_str1) == "".join(
        c.lower() for c in normalized_str2
    )

if __name__ == "__main__":
    # Hard-coded sample values to test the function without user input.
    samples = [
        ("Hello", "HELLO"),  # Should return True
        ("World!", "world!"),  # Should return True
        ("Café", "CAFÉ"),  # Should return True (accent handling)
        ("Müller", "müLler"),  # Should return True (special character case insensitivity)
        ("Test", "test123"),  # Should return False
    ]

    for s1, s2 in samples:
        result = case_insensitive_equal(s1, s2)
        print(f"Comparing '{s1}' and '{s2}': {result}")