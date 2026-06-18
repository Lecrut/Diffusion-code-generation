def extract_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from a given string, ignoring words 
    that contain no alphabetic characters (e.g., punctuation-only strings).

    Args:
        text (str): The input string to process.

    Returns:
        List[str]: A list containing the first character of valid words in order.
    """
    result = []
    
    # Split into tokens handling multiple spaces and newlines as delimiters effectively
    # We iterate through characters manually or use regex with a specific pattern 
    # to ensure we capture only alphabetic starts after non-word sequences, skipping pure punctuation.

    current_word_chars = []
    
    for char in text:
        if char.isalpha():
            current_word_chars.append(char)
        else:
            # If the word is empty (only punctuations or digits without letters encountered yet), skip
            if not current_word_chars and char.isdigit() == False: 
                continue
            
            # When a non-alphabetic character breaks a sequence, process it only if we have collected at least one letter?
            # Actually, let's refine logic to collect sequences of chars then filter.

    pass 

def extract_first_letters_v2(text: str) -> list[str]:
    """
    Refactored version using regex for cleaner tokenization and validation.
    
    Words are defined here as any sequence containing at least one alphabetic character.
    We split the text into potential words, filter those without letters, then take first char.
    """
    import re
    
    # Split by whitespace or punctuation to get candidate "words" (sequences of non-whitespace)
    tokens = re.split(r'[\s\W]+', text.strip())
    
    output_list = []
    
    for token in tokens:
        if not token:
            continue

if __name__ == '__main__':
    pass
