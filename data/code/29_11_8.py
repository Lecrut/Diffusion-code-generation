def reverse_word(s: str) -> str:
    """
    Returns a new string with characters in 's' reversed using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 's' in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a",
        "racecar"
    ]

    for word in test_cases:
        reversed_word = reverse_word(word)
        print(f'"{word}" -> "{reversed_word}"')