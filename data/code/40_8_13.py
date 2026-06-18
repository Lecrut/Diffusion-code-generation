def extract_first_letters(text: str) -> list[str]:
    """
    Extracts a list of strings, where each string is the first letter 
    of a word in the input text. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of single-character strings representing the first letters 
                  of valid words found in the input.
    """
    import re
    
    # Split the text into tokens based on whitespace and punctuation boundaries,
    # but we need a more robust approach to isolate "words".
    # We will use regex to find sequences of alphanumeric characters (letters/digits).
    # This naturally ignores words that are only punctuation.
    
    matches = re.findall(r'\b\w+\b', text)
    
    result_list = []
    for match in matches:
        if len(match) > 0 and not match[0].isdigit(): 
            # We take the first character, ensuring it's a letter (not digit).
            # The problem implies "first letter", so digits are excluded.
            char = match[0]
            result_list.append(char)
            
    return result_list

if __name__ == '__main__':
    sample_text = """Hello, world! This is a test... 
    with numbers 123 and symbols @#$%^&*()."""

    output = extract_first_letters(sample_text)
    
    print("Input:", repr(sample_text))
    print("Output:", output)