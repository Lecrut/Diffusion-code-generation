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
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "Python programming",
        "",
        "a"
    ]

    print("Original Word | Reversed Word")
    print("-" * 30)
    
    for word in test_cases:
        reversed_word = reverse_word(word)
        print(f"{word!r:<20} | {reversed_word!r}")