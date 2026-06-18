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
    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "a"
    ]

    print("Original Word | Reversed Word")
    print("-" * 30)
    
    for word in test_cases:
        reversed_word = reverse_word(word)
        print(f"{word!r:<25} | {reversed_word!r}")