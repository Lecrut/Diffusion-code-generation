def reverse_word(text: str) -> str:
    """
    Returns a new string with the characters of the input reversed.
    Uses slicing for maximum efficiency as per requirements.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the reversed characters.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello",
        "Python Programming",
        "",
        "a" * 100,
        "Reverse this string!"
    ]

    print("Testing reverse_word function:")
    for s in samples:
        reversed_s = reverse_word(s)
        print(f'Original: "{s}" -> Reversed: "{reversed_s}"')