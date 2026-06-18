def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string efficiently.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello world",
        "",
        "a" * 1000,  # Large string to demonstrate efficiency
        "Python programming is fun!",
    ]

    results = []
    for text in test_cases:
        reversed_text = reverse_string(text)
        results.append(f'Input: "{text}"\nOutput: "{reversed_text}"')
    
    print('\n'.join(results))