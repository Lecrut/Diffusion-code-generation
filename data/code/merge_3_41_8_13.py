def format_string_versions(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original string.
    2. All uppercase version.
    3. Sentence case version (first letter capitalized, rest lowercase).

    Uses string slicing and built-in methods to achieve this transformation.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A comma-separated string containing the original, all-caps, 
             and sentence-case versions of the input.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return "Original,,All caps"

    # Get uppercase version using built-in method
    upper_version = text.upper()
    
    # Create lowercase base for sentence case logic
    lower_base = text.lower()
    
    # Apply string slicing to capitalize the first letter and keep rest as is, 
    # then combine with remaining characters from original (lowercased) if needed.
    # However, standard approach using built-ins: slice [0] + slice[1:].upper() for title case logic?
    # The task asks specifically for "sentence-case". Standard sentence case means first letter uppercase, rest lowercase.
    
    # Using slicing to construct the sentence case version explicitly as requested by constraint emphasis on slicing/methods usage contextually:
    # First char capitalized from original or lowercased? Usually derived from input logic but strictly following built-in methods for transformation:
    if len(lower_base) > 0:
        first_char = lower_base[0].upper()
        rest_chars = lower_base[1:]
        sentence_version = first_char + "".join(rest_chars).lower() # join is a method, slicing used on index. 
        # Wait, simpler pure string operations without loop if possible? 
        # "capitalize()" exists but task implies using slice/methods logic manually or standard ones allowed.
        # Let's use capitalize which uses internal logic but satisfies built-in requirement better than manual loops unless specified otherwise.
        # Re-reading: "uses string slicing and built-in methods". Capitalize is a method. 
        # But to be safe with explicit slice usage demonstration for the 'rest' part if needed, let's stick to standard library behavior which uses internal logic but we can demonstrate slices in other parts or just use capitalize().
        # Actually, sentence case definition: First letter upper, rest lower.
        # Python str.capitalize() does exactly this (lowercases everything else). 
        # Let's verify if manual slicing is safer for "uses string slicing" constraint interpretation.
        # If I do text[0].upper() + text[1:].lower(), that uses slices and methods perfectly.
        
        sentence_version = lower_base[0].upper() + "".join(lower_base[i] for i in range(1, len(lower_base))) 
        # Wait, join is a method but requires iteration. Is there a pure slice way?
        # text.lower().capitalize() is the most robust built-in solution that uses methods implicitly.
        # But to explicitly show slicing usage as per task hint:
        
    else:
        sentence_version = ""

    return f"{text},{upper_version},{sentence_version}"

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = format_string_versions(sample_text)
    print(result)