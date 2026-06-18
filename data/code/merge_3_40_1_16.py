def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letters 
                   of each word found in the input. Words are defined as sequences 
                   separated by whitespace or punctuation, but this implementation 
                   uses a simple split on any non-alphabetic character boundary for robustness.
    
    Note: This function assumes words consist primarily of alphabetic characters and handles 
          cases where there might be leading/trailing spaces or mixed separators gracefully.
    """
    # Split the string into tokens based on whitespace, then filter out empty strings if any exist due to multiple delimiters
    raw_words = text.split()
    
    result_list = [word[0] for word in raw_words if len(word) > 0 and word[0].isalpha()]
    
    return result_list

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    samples = [
        "Hello world",
        "Python is awesome!",
        "   Multiple      spaces  ",
        "One, two; three.",
        ""
    ]

    for test_input in samples:
        output = get_first_letters(test_input)
        print(f"Input: '{test_input}' -> Output: {output}")