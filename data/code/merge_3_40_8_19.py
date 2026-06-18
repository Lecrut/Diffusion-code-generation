def get_first_letters(text):
    """
    Takes a string and returns a list of strings containing the first letter 
    of each word, ignoring words that contain no alphabetic characters (e.g., punctuation-only).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list where each element is the lowercase first letter of a valid word.
                   Valid words are defined as sequences containing at least one alphabetic character.
    """
    # Split the text into potential tokens based on whitespace or punctuation boundaries, 
    # but we need to be careful with contractions like "don't". A robust approach is to split by non-alphanumeric chars first,
    # then filter and take the first letter of alphanumeric sequences that exist.
    
    cleaned_text = []
    
    # Replace all characters that are not letters or digits with a space separator
    import re
    
    tokens = re.split(r'[^a-zA-Z0-9]+', text.strip())
    
    result_letters = []
    
    for token in tokens:
        if len(token) == 0:
            continue
        
        # We consider the first character that is alphabetic as the start of a "word" 
        # to avoid issues with contractions (e.g., "don't" -> ['d', 'o', ...] should be handled or decided).
        # The prompt implies standard word definition. Usually, "don't" counts as one word starting with 'D'.
        # However, strict splitting often breaks it. Let's stick to the most logical interpretation:
        # A sequence of alphanumeric characters is a word. Splitting only by non-alphanumeric chars 
        # keeps contractions together unless spaces separate them in the original string which aren't present here?
        # Actually, re.split with no match for '!' inside "don't" will keep it as one token if there's no space before/after '!'.
        
        first_char = None
        
        # Find the index of the first alphabetic character to handle edge cases like "'hello' -> h" or "!hey" -> h
        alpha_idx = -1
        for i, char in enumerate(token):
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                first_char = char.lower()
                break
        
        # If a word has no alphabetic character (e.g., "!!!", "---"), do not add it.
        if first_char is None:
            continue
            
        result_letters.append(first_char)

    return result_letters

if __name__ == '__main__':
    samples = [
        "Hello, world!", 
        "It's a beautiful day.", 
        "... !!! ...", 
        "Python 3.9! # coding", 
        "No words here!!!"
    ]

    for sample in samples:
        output_list = get_first_letters(sample)
        print(f"Input: '{sample}'")
        print(f"Output: {output_list}")
        print("---")