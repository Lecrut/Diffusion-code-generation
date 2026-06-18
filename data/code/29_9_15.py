def reverse_string(word: str) -> str:
    """
    Reverses a given string using Python's slicing capabilities.
    
    Args:
        word (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Python",
        "Hello, World!",
        "",
        "a-b-c-d-e"
    ]

    print("Original Words and Their Reverses:")
    for word in samples:
        reversed_word = reverse_string(word)
        print(f"'{word}' -> '{reversed_word}'")