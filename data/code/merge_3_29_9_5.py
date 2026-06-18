def reverse_word(word: str) -> str:
    """
    Reverses a single word using Python's slicing capabilities.
    
    Args:
        word (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello",
        "Python programming is fun!",
        "",
        "a"
    ]

    print("Original Words and their Reverses:")
    print("-" * 40)
    
    for word in samples:
        reversed_word = reverse_word(word)
        print(f'"{word}" -> "{reversed_word}"')