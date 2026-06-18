def extract_first_letters(text: str) -> list[str]:
    """
    Extracts a list of strings where each string is the first letter 
    of a word in the input text, ignoring words that contain only punctuation or whitespace.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list containing the first character of valid words found in the text.
                   Characters are converted to lowercase for consistency unless specified otherwise.
                   Words with no alphabetic characters (e.g., punctuation-only) are skipped.
    
    Example:
        >>> extract_first_letters("Hello, world! ...")
        ['h', 'w']
    """
    import re
    
    # Split the text into tokens based on whitespace and non-alphanumeric separators
    words = re.findall(r'\S+', text)
    
    result_list = []
    
    for word in words:
        # Check if the word contains at least one alphabetic character
        has_alpha = any(char.isalpha() for char in word)
        
        if not has_alpha:
            continue
            
        # Get the first alphabetic character from the word
        first_char = ''
        for char in word:
            if char.isalpha():
                first_char = char.lower()  # Convert to lowercase as per common convention
                break
        
        result_list.append(first_char)
    
    return result_list

if __name__ == '__main__':
    sample_text = "Hello, world! ... This is a test. @#$% &*()"
    output_result = extract_first_letters(sample_text)
    print(output_result)  # Expected: ['h', 'w', 't', 'i']