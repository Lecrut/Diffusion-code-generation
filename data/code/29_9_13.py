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
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "Python",
        "reversed_string",
        "",
        "a"
    ]

    print("Reversing words using Python slicing:\n")
    
    for word in test_cases:
        reversed_word = reverse_word(word)
        print(f'Original: "{word}" -> Reversed: "{reversed_word}"')