def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings, each being the first 
                   non-whitespace character from each corresponding word.
                   
    Example:
        >>> get_first_letters("Hello World")
        ['H', 'W']
        >>> get_first_letters("")
        []
        >>> get_first_letters("   spaced words here  ")
        ['s', 'w', 'h']
    """
    return [word[0] for word in text.split()]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required.
    samples = ["Hello World", "", "   spaced words here  ", "Python Programming"]
    
    print("First letters of various inputs:")
    for test_input in samples:
        result = get_first_letters(test_input)
        print(f'Input: "{test_input}" -> Output: {result}')