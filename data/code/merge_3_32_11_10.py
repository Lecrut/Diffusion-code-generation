def calculate_phrase_length(phrase: str) -> int:
    """
    Returns an integer that is equal to length of input phrase, which may contain spaces 
    or special characters if they exist in string argument. Uses built-in len() function 
    for optimized performance as it operates directly on the underlying object's internal state.
    
    Args:
        phrase (str): A string input
    
    Returns:
        int: Length of input phrase
    """
    return len(phrase)

if __name__ == '__main__':
    # Sample values for testing without external inputs or files
    test_cases = ["Hello", "Python 3.9 is great.", "!@#$%", "", "   spaces here   "]
    
    results = []
    for phrase in test_cases:
        length = calculate_phrase_length(phrase)