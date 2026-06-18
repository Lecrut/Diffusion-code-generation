def get_first_letters(text: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary where keys are words 
    and values are their respective first letters (lowercase).
    
    Punctuation is ignored when determining the first letter.
    Words are defined as sequences of alphabetic characters separated by non-alphabetic characters or spaces.

    Args:
        text (str): The input string to process.

    Returns:
        dict[str, str]: A dictionary mapping words to their first letters in lowercase.
    """
    result = {}
    
    # Split the text into tokens based on whitespace and punctuation is handled by filtering chars during processing
    # We will iterate through characters to build valid words
    
    current_word_chars = []
    
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check if character is alphabetic
            current_word_chars.append(char)
        else:
            # If we have a non-empty word, process it and reset
            if len(current_word_chars) > 0:
                first_letter = ''.join([c for c in current_word_chars]).lower()[:1]

if __name__ == '__main__':
    pass
