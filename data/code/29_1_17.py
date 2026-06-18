def reverse_word(s: str) -> str:
    """
    Returns the reversed version of a single string argument.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_strings = [
        "hello",
        "Python programming",
        "",
        "a" * 100,
        "!@#$%"
    ]

    for original in sample_strings:
        reversed_result = reverse_word(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_result}"\n')