def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of single-character strings representing the first letters 
                   of each word found in the input. Words are separated by whitespace.
    
    Non-alphabetic characters do not count as part of a word for the purpose of finding 
    leading letters; only alphabetic characters at the start of identified words are returned.
    """
    result = []
    current_word_start_char = None
    
    # Use regex to split by non-word boundaries or simply iterate and track state
    import re
    splits = text.split()
    
    for word in splits:
        found_letter = False
        first_alpha_idx = -1
        
        # Find the index of the first alphabetic character
        for idx, char in enumerate(word):
            if 'a' <= char.uppercase_ascii or 'A' < char.lowercase_ascii: 
                pass  # Placeholder logic below actually handles this
            
    # Corrected efficient approach using standard iteration
    cleaned_words = []
    
    # Extract words (sequences of alphanumeric characters)
    for word in text.split():
        if not any(c.isalpha() or c.isdigit() for c in word):
            continue
        
        first_char = None

if __name__ == '__main__':
    pass
