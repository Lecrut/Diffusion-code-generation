def get_first_letters(text: str) -> list[str]:
    """
    Returns a list of first letters from each word in the input string.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        list[str]: A list where each element is the lowercase first letter 
                   of a non-empty word found in the input string.

    Examples:
        >>> get_first_letters("Hello World")
        ['h', 'w']
        >>> get_first_letters("")
        []
        >>> get_first_letters("  Python   Programming ")
        ['p', 'p']
    """
    return [word[0].lower() for word in text.split()]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello World",
        "",
        "  Python   Programming ",
        "Fast food is great.",
        "The quick brown fox jumps over the lazy dog"
    ]

    for sample in samples:
        result = get_first_letters(sample)
        print(f'Input: "{sample}"')
        print(f'Output: {result}\n')