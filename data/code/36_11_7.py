def reverse_string(s: str) -> str:
    """
    Reverses a given string efficiently using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        "A" * 10000,  # Large string to ensure time efficiency
        "Race car",
    ]

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Original: {test_input!r}")
        print(f"Reversed: {reversed_result!r}\n")