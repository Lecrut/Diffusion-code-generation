def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the 
                   first letters of each detected word.
                   
    Words are defined as sequences separated by whitespace or punctuation,
    and only alphabetic characters at the start of a sequence are considered.
    """
    import re
    
    # Split string into words based on non-alphabetic boundaries to ensure robustness
    # This regex finds all contiguous alphabetic character sequences (words)
    words = re.findall(r'[a-zA-Z]+', text.lower())
    
    return [word[0] for word in words if len(word) > 0]

if __name__ == '__main__':
    sample_input = "Hello, world! This is a test of the optimized function."
    result = get_first_letters(sample_input)
    print(result)