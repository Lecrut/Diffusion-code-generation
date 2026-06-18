def reverse_word(word: str) -> str:
    """
    Reverses a given word using Python's string slicing capabilities.
    
    Args:
        word (str): The input word to be reversed.
        
    Returns:
        str: The reversed version of the input word.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    sample_words = [
        "Python",
        "Hello, World!",
        "DataScience"
    ]

    print("Original Words and their Reversed Versions:")
    for original in sample_words:
        reversed_word = reverse_word(original)
        print(f"'{original}' -> '{reversed_word}'")