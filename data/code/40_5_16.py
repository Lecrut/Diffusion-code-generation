def first_letters_of_words(text: str) -> dict:
    """
    Takes a string and returns a dictionary where keys are words 
    and values are their respective first letters (lowercased).
    Punctuation is ignored when determining the first letter.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        dict: A dictionary mapping each word to its first letter.
    """
    import re
    
    # Split the text into tokens, keeping whitespace but removing punctuation from words
    # We use regex to find all sequences of alphanumeric characters and apostrophes (for contractions)
    tokens = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)*", text)
    
    result_dict = {}
    
    for token in tokens:
        # Clean the token to ensure only letters remain for finding the first letter
        clean_token = ''.join(char.lower() for char in token if char.isalpha())
        
        if not clean_token:
            continue
            
        word_key = token  # Keep original token as key (e.g., "don't")
        first_letter_value = clean_token[0]
        
        result_dict[word_key] = first_letter_value
        
    return result_dict

if __name__ == '__main__':
    sample_input = "Hello, world! This is a test. Don't forget your 'books'."
    
    output_result = first_letters_of_words(sample_input)
    
    print("Input:", repr(sample_input))
    print("\nOutput Dictionary:")
    for word, letter in sorted(output_result.items()):
        print(f"  '{word}': {repr(letter)}")