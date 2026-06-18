def reverse_word(text: str) -> str:
    """
    Reverses a single word (string) efficiently using slicing.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = ["hello", "Python 3.9", "!olleh"]
    
    print("Testing reverse_word function:")
    for test_input in samples:
        reversed_result = reverse_word(test_input)
        print(f"Input: '{test_input}' -> Output: '{reversed_result}'")