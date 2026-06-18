import string

def first_letters_of_words(text: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary where keys are words 
    (stripped of leading/trailing punctuation/spaces) and values 
    are the uppercase letter that follows immediately after any initial punctuations.
    
    The function ignores non-alphabetic characters when determining the first character,
    effectively skipping leading punctuation to find the first alphabetic letter for each word.

    Parameters:
        text (str): Input string containing words and possibly punctuation.

    Returns:
        dict[str, str]: A dictionary mapping cleaned words to their normalized starting letters.
    
    Example usage: 
        first_letters_of_words("Hello!, world..") returns {"hello": "H", "world": "W"}
    """
    result = {}

    # Split into potential tokens based on whitespace and punctuation separation logic handled in loop
    words_raw = []
    current_word_chars = []

if __name__ == '__main__':
    pass
