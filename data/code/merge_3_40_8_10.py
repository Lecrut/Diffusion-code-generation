def extract_first_letters(text: str) -> list[str]:
    """
    Extracts a list of strings where each string is the first letter 
    of a word in the input text, ignoring words that contain only punctuation or whitespace.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list containing the first letter of each valid word found.
                   If no letters are extracted, returns an empty list.
    """
    words = text.split()
    result = []

    for word in words:
        # Check if the string is not just whitespace (split already handles this)
        # and contains at least one alphabetic character before any punctuation logic needed here? 
        # The requirement says "words containing only punctuation are correctly handled".
        # Standard split splits by whitespace. We need to check the word content itself.
        
        if len(word.strip()) == 0:
            continue
            
        first_char = word[0]
        is_letter = 'a' <= first_char <= 'z' or 'A' <= first_char <= 'Z'

        # If the very first character of a split token isn't a letter, 
        # we check if there are any letters in the whole string. 
        # However, typically "words containing only punctuation" implies tokens like "...", "---".
        # Let's refine: Iterate through characters to find the first actual alphabetic char.
        
        found_letter = False
        for char in word:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                result.append(char)
                found_letter = True
                break
        
    return result

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input.
    samples = [
        "Hello, world! How are you?",
        "... !!! --- ...",
        "One... two!!! three...",
        "No letters here!",
        "Mixed 123 abc def!"
    ]

    for sample in samples:
        output = extract_first_letters(sample)
        print(f"Input: {sample!r}")
        print(f"Output: {output}\n")