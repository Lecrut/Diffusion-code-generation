def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letters 
                   of each word found in the input. Words are defined as sequences 
                   separated by whitespace, and only alphabetic characters at the start 
                   of a sequence are considered (ignoring leading non-alphabetic chars).
    """
    words = text.split()
    
    # List comprehension to extract first letter if it's an alphabet character
    return [word[0] for word in words if len(word) > 0 and word[0].isalpha()]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string."
    
    result = get_first_letters(sample_text)
    
    print(f"Input: '{sample_text}'")
    print(f"Output: {result}")