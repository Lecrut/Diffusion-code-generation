def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string, preserving case elsewhere.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letters of words capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split into words based on whitespace while preserving original spacing structure logic implicitly via join
    parts = text.split()
    
    # Capitalize each word's first letter and ensure the rest remains lowercase or mixed as per requirement? 
    # Note: The prompt says "preserving the rest of the casing". Standard title case usually lowercases the rest, 
    # but here we strictly capitalize only the FIRST letter. However, standard behavior for such tasks often implies
    # converting non-first letters to their original case if they were already there (which is trivial) or just leaving them?
    # Re-reading: "capitalizes only the first letter of each word". 
    # If input is "hello WORLD", output should be "Hello World" -> 'H' from 'h', 'e' stays, etc.
    # Actually, if we strictly follow "only capitalize the first letter", then "HELLO" becomes "HelLo"? 
    # Or does it mean standard Title Case? Usually these tasks imply standard capitalization rules (First upper, rest lower).
    # But let's look at the constraint: "preserving the rest of the casing". This implies if input is 'HeLLo', output should be 'HeLLo' -> 'H'e'Ll'O'? 
    # No, that would mean changing nothing. The most logical interpretation for a utility script without complex regex requirements
    # and given typical expectations: Capitalize first letter (upper), keep the rest EXACTLY as they are in input?
    # OR does it mean standard Title Case where we fix casing? 
    # Let's assume strict literal interpretation of "preserving": Input 'aBc' -> Output 'AbC'. 
    # But wait, if I have 'abc', output should be 'Abc'. If 'ABC', output 'AbC'?
    # Actually, the most robust and common definition for this specific phrasing in coding challenges is:
    # First letter becomes Upper. All other letters remain exactly as they were in the input string (including upper/lower mix).
    
    result_parts = []
    for word in parts:
        if not word:
            continue
            
        first_char = word[0]
        rest_chars = word[1:]
        
        # Capitalize only the first char, leave the rest untouched to preserve their casing exactly as input
        new_word = first_char.upper() + "".join(char for char in rest_chars) 
        result_parts.append(new_word)

    return " ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values that require no user input, network access, or files.
    samples = [
        "hello world",
        "Python Is Awesome",
        "  multiple   spaces ",
        "ALL LOWERCASE",
        "MiXeD CaSe WoRlDs"
    ]

    for sample in samples:
        capitalized_result = capitalize_words(sample)
        print(f'Input : "{sample}"')
        print(f'Output: "{capitalized_result}"\n')