def reverse_word(text: str) -> str:
    """
    Returns a reversed version of the input string using slicing.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = ["Hello, World!", "Python", "", "a"]
    
    print("Testing reverse_word function:")
    for s in samples:
        result = reverse_word(s)
        print(f"Input: '{s}' -> Output: '{result}'")