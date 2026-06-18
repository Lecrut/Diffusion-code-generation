def reverse_word(s: str) -> str:
    """
    Returns the reversed version of a single word (string).
    
    Uses slicing to achieve maximum efficiency as requested.
    
    Args:
        s (str): The input string representing a single word.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = ["hello", "Python", "world!", "a"]
    
    for word in samples:
        reversed_word_result = reverse_word(word)
        print(f"Original: '{word}' -> Reversed: '{reversed_word_result}'")