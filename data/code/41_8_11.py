def format_string(text: str) -> str:
    """
    Returns a formatted string containing three versions of the input text,
    separated by commas: original, all-caps, and sentence-case.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A comma-separated string with 'original', 'UPPERCASE', and 
             'Sentence Case' versions of the input.
    """
    upper = text.upper()
    # Create sentence case by capitalizing only the first letter if it exists, otherwise leave as is (or handle empty)
    # Standard sentence case: capitalize first character, lower rest; but typically for strings 
    # we just title-case or manually adjust. The prompt implies a standard "sentence-case" transformation
    # which usually means CapitalizeFirst(LowerRest). If the string has no letters in it to be changed? 
    # We'll assume standard behavior: capitalize first char, lowercase rest unless there are other caps intended 
    # but typically sentence case is TitleCase with only one word capitalized if single word.
    # Using a simple approach: Capitalize first letter of entire text and lower the rest for pure sentence-case interpretation per prompt context often expecting 'Sentence Case'.
    
    if len(text) == 0 or not any(c.isalpha() for c in text):
        sentence = ""
    else:
        chars = list(text)
        # Capitalize first character that is a letter, and lowercase the rest (except maybe non-letters?) 
        # A robust simple version: just capitalize first char if alpha, lower the remaining alphas.
        i = 0
        while i < len(chars):
            c = chars[i]
            if not c.isalpha():
                break
            else:
                # Capitalize only the very first letter found that is alphabetic? 
                # Or standard title casing but for single sentence logic. Let's do: First char cap, rest lower (for non-alpha keep as is).
                pass
            
        # Re-implementing simply using built-in methods if possible or manual loop to ensure correct behavior without importing extra libraries like 'str.maketrans' which might be considered advanced enough? 
        # Actually str.capitalize() does exactly this: first char upper, rest lower.
        sentence = text.capitalize()

    return f"{text}, {upper}, {sentence}"

if __name__ == '__main__':
    sample_text = "hello world"
    result = format_string(sample_text)
    print(result)