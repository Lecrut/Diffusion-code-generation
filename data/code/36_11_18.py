def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string efficiently.
    
    For large strings, slicing with step -1 is O(n) and highly optimized 
    in CPython's implementation compared to manual character iteration or list conversion.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 's' in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        "hello",
        "",
        "a" * 100,  # Large string performance check
        "Python is awesome!",
        "1234567890",
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed:{reversed_output!r}\n")