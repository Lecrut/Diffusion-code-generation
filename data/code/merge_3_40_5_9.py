def get_first_letters(word_string: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary where keys are words 
    (excluding punctuation) and values are their respective first letters.
    
    Punctuation is ignored when determining the word boundaries and 
    the first letter of each word. The function handles multiple spaces 
    between words correctly by treating them as separators, not part of the text.

    Args:
        word_string (str): A string containing words separated by whitespace or punctuation.

    Returns:
        dict[str, str]: A dictionary with cleaned words as keys and their first letters as values.
                         If a key is already present in the dictionary, it will be overwritten 
                         if encountered again under different conditions; however, since this function 
                         maps unique words to single characters (ignoring case for uniqueness unless specified),
                         we assume standard behavior where identical cleaned strings map to the same letter.

    Example:
        >>> get_first_letters("Hello, world! How are you?")
        {'hello': 'h', 'world': 'w', 'how': 'h', 'are': 'a', 'you': 'y'}
    """
    
    # Replace non-alphanumeric characters with spaces to isolate words properly
    cleaned_string = ''.join(char if char.isalnum() else ' ' for char in word_string)

    # Split the string into individual words based on whitespace
    words_list = [word.strip().lower() for word in cleaned_string.split()]

    result_dict: dict[str, str] = {}

    for word in words_list:
        if not word:  # Skip empty strings resulting from consecutive spaces or leading/trailing punctuation
            continue
        
        first_char = word[0].upper()
        
        key_lower = word.lower().strip('.,!?;:"\'-')
        result_dict[key_lower] = first_char

    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "Hello, world! How are you?",
        "Python 3.10 is great!",
        "The quick brown fox jumps over the lazy dog.",
        "",
        "... !!! ???",
        "One two three four five."
    ]

    for sample in samples:
        print(f"Input: '{sample}'")
        output = get_first_letters(sample)
        print(f"Output: {output}")