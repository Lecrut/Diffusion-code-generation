def reverse_word(word: str) -> str:
    """
    Reverses a given word using Python's slicing capabilities.
    
    Args:
        word (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "a"
    ]

    print("Reversed Words:")
    for original in test_cases:
        reversed_word = reverse_word(original)
        print(f"'{original}' -> '{reversed_word}'")