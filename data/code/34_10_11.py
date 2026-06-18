def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text
    
    words = text.split()
    
    # Capitalize the first letter and keep the rest as is for non-empty strings
    def process_word(word):
        if len(word) > 1:
            return word[0].upper() + word[1:]
        else:
            return word.upper()
            
    capitalized_words = [process_word(w) for w in words]
    
    # Rejoin the words with a single space to preserve original spacing structure roughly,
    # but standardizing on single spaces between words as per typical "capitalize" behavior.
    # If strict preservation of multiple spaces is needed without collapsing them:
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world! this is a test string."
    
    result = capitalize_words(sample_input)
    
    print(f"Input:  '{sample_input}'")
    print(f"Output: '{result}'")