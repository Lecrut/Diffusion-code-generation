def reverse_word(text):
    """
    Reverses a single word (or string) efficiently using slicing.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of the original string in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello",
        "Python Programming",
        "   spaces around word  ",
        ""
    ]
    
    print("Testing reverse_word function:")
    for test_input in samples:
        reversed_output = reverse_word(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{reversed_output}'\n")