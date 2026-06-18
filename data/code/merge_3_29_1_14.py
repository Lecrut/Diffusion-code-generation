def reverse_word(text: str) -> str:
    """
    Returns the reversed version of the input string using slicing,
    which is the most Pythonic and efficient method available in CPython.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: A new string with characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_inputs = ["hello", "Pythonic!", ""]
    
    for word in sample_inputs:
        reversed_word = reverse_word(word)
        print(f"Original: '{word}' -> Reversed: '{reversed_word}'")