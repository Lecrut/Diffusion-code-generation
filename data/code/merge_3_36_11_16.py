def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string in a time-efficient manner.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        "A" * 10000  # Large string to ensure efficiency
    ]

    results = []
    for text in test_cases:
        reversed_text = reverse_string(text)
        results.append(f'Original: "{text}" -> Reversed: "{reversed_text}"')
    
    print('\n'.join(results))