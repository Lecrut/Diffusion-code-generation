def reverse_word(word: str) -> str:
    """
    Reverses a single word using Python's string slicing.
    
    Args:
        word (str): The input word to be reversed.
        
    Returns:
        str: The reversed version of the input word.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "Python",
        "reverse_this_string!",
        "a"
    ]

    print("Word Reversal Results:")
    for original in test_cases:
        reversed_word = reverse_word(original)
        print(f"'{original}' -> '{reversed_word}'")