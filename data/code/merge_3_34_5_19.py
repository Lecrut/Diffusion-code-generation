def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in the string, 
    while ensuring that no other letters within any word are capitalized.
    
    This function handles multiple words separated by whitespace or common separators like hyphens,
    treating them as distinct units for capitalization purposes if they appear consecutively without spaces,
    but primarily focuses on standard space-separated sentences and phrases where only the first letter 
    of each 'word' (sequence of non-space characters) is capitalized.

    Args:
        text (str): The input multi-word string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized, others remaining lowercase.
    
    Example:
        >>> capitalize_first_letter_only("hello world")
        'Hello World'
        >>> capitalize_first_letter_only("this is a test sentence.")
        'This Is A Test Sentence.'
    """
    if not text or not isinstance(text, str):
        return ""

    # Split the string into words based on whitespace. 
    # We keep track of original separators to reconstruct properly if needed,
    # but for standard readability in this context, space separation is assumed as word delimiter.
    
    parts = []
    current_word_parts = [text[0].lower()]  # Start with first character lowercased
    
    i = 1
    while i < len(text):
        char = text[i]
        
        if not char.isalpha():
            # Non-alphabetic characters act as delimiters between words in this logic context,
            # or simply reset the word building. However, to strictly follow "first letter only",
            # we treat any sequence of alphabets as a potential word unit for capitalization rules.
            
            if current_word_parts and not char.isalpha():
                parts.append("".join(current_word_parts))
                current_word_parts = []
        
        elif len(current_word_parts) == 0:
            # First letter of the string should be capitalized regardless of position in flow, 
            # but we handle it here as part of a new word sequence.
            if char.isupper():
                parts.append(char.lower())
            else:
                current_word_parts = [char.upper()]
        elif len(current_word_parts) > 0 and not char.isalpha():
            # Separator encountered within what might be considered one token or just reset logic?
            # Let's stick to simple word definition: sequence of letters.
            parts.append("".join(current_word_parts))
            current_word_parts = [char.lower()] if i + 1 < len(text) and text[i+1].isalpha() else [] 
        elif char.isupper():
            # If we are in the middle of a word, ensure only first is upper.
            parts.append("".join(current_word_parts))
            current_word_parts = [char.lower()] if i + 1 < len(text) and text[i+1].isalpha() else [] 
        elif char.islower():
            # Continue building the lowercased rest of the word
            pass
            
        i += 1
    
    # Handle remaining characters in last segment
    current_word_parts = [text[-1]] if not parts or (not any(p for p in parts)) and text else []

    # Re-evaluating logic with a cleaner approach using regex-like splitting manually to ensure correctness.
    
    words = text.split()
    result_words = []
    
    for word in words:
        if len(word) == 0: continue
        
        first_char = word[0]
        rest_chars = word[1:] 
        
        # Capitalize only the first letter, make sure it's uppercase. 
        # The rest of the letters should be lowercase to ensure "first letter ONLY" rule is met strictly per word.
        
        if len(word) > 0:
            capitalized_word = first_char.upper() + "".join(c.lower() for c in rest_chars if not c.isalpha())
            
            # Wait, the requirement says "capitalize the first letter only". 
            # Does it mean ONLY capitalize that one? Or does it imply standard title case but strictly no other caps?
            # Standard interpretation: First char upper, others lower.
            
            capitalized_word = word[0].upper() + "".join(c.lower() for c in rest_chars) if len(word) > 1 else first_char.upper()
        result_words.append(capitalized_word)

    return " ".join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "hello world",
        "this is a test sentence.",
        "python programming language",
        "  multiple   spaces here ",
        "no capitalization needed"
    ]

    for sample in samples:
        output = capitalize_first_letter_only(sample)
        print(f'Input: "{sample}"')
        print(f'Output: "{output}"\n')