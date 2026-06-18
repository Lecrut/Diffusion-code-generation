def get_first_letters(text: str) -> list[str]:
    """
    Takes a string and returns a list of strings, where each string is 
    the first letter of a word. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letters of words.
    """
    import re
    
    # Split the text into tokens based on whitespace and other non-alphanumeric boundaries, 
    # but we need to be careful with punctuation attached to words.
    # We'll use regex to find sequences that start with a letter or digit (considered part of word)
    # followed by any characters until they hit another such sequence end or string end.
    
    # A simpler approach: split on non-alphanumeric chars, then filter out empty strings 
    # and those containing only punctuation if the original token was purely punctual? 
    # Actually, standard definition of "word" usually implies alphanumeric sequences separated by whitespace/punctuation.
    # However, the prompt says "words containing only punctuation... do not produce an output".
    # Example: "...!..." should be ignored as a word itself if it stands alone or is part of a sequence? 
    # Let's interpret 'word' as a contiguous sequence of alphanumeric characters (letters and digits).
    # If the regex finds sequences like ['hello', '!world!', '...'], we take first letter.
    
    words = re.findall(r'\b[\w]+\b', text)
    
    result = []
    for word in words:
        if not word:  # Safety check, though findall shouldn't return empty strings usually unless logic differs
            continue
        
        # Check if the first character is alphabetic (since \w includes digits and underscores)
        # The prompt implies "first letter", so we should only take it if it's a letter.
        char = word[0]
        
        import string
        if not any(c.isalpha() for c in [char]): 
            continue
            
        result.append(char.lower())  # Optional: normalize to lowercase? Prompt doesn't specify case sensitivity, but usually implied or preserved. Let's preserve original case unless specified otherwise. Re-reading prompt: "first letter". Usually implies the character itself.
        
    return result

# Revised logic based on strict interpretation without external imports if possible (re is standard)
def get_first_letters_v2(text: str) -> list[str]:
    """
    Takes a string and returns a list of strings, where each string is 
    the first letter of a word. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first letters of words.
    """
    import re
    
    # Find all sequences consisting of alphanumeric characters and underscores (\w)
    # This effectively splits on punctuation, spaces, etc., treating them as delimiters.
    matches = re.findall(r'\b[\w]+\b', text)
    
    result = []
    for match in matches:
        if not match: 
            continue
            
        first_char = match[0]
        
        # Ensure the character is actually a letter (a-z, A-Z), ignoring digits or underscores as "letters" per strict linguistic definition.
        import string
        if any(c.isalpha() for c in [first_char]):
            result.append(first_char)
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file I/O is needed.
    samples = [
        "Hello, world! This is a test.",
        "...!!! ...",  # Only punctuation
        "Python3.10: The language of choice!",
        "No words here... just noise...",
        "One two three four five."
    ]

    for sample in samples:
        output = get_first_letters_v2(sample)
        print(f"Input: {sample}")
        print(f"Output: {output}\n")