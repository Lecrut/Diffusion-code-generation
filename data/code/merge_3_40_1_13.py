def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    The function splits the text into words, strips whitespace from each part to isolate letters,
    and extracts the first character if it exists. It uses list comprehension for efficiency.

    Args:
        text (str): A single string potentially containing multiple words separated by spaces or punctuation.

    Returns:
        List[str]: A list of strings where each element is the first letter found in a word, 
                   otherwise an empty string if no valid character exists at that position.
    
    Example:
        >>> get_first_letters("Hello World!")
        ['H', 'W']
    """
    words = text.split()
    return [word[0] for word in words if len(word) > 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Python is awesome",
        "Hello, World!",
        "",
        "   Multiple   spaces   here ",
        "One word"
    ]

    for test_input in samples:
        result = get_first_letters(test_input)
        print(f'Input: "{test_input}" -> Output: {result}')