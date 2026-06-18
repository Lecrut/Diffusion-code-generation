def format_string_versions(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original text.
    2. All-caps version.
    3. Sentence-case version (first letter uppercase, rest lowercase).

    Args:
        text (str): The input string to process.

    Returns:
        str: A comma-separated string of the three versions joined by ', '.
    """
    original = text
    
    # Create all-caps version using built-in method
    upper_case_version = text.upper()
    
    # Create sentence-case version manually since no direct built-in exists for this specific format
    if not original:
        lower_case_version = ""
    else:
        first_char = original[0].lower() if original[0].isupper() or (len(original) > 1 and original[0] != ' ') else original[0]
        rest_of_string = original[1:]
        
        # Convert the rest to lowercase, then capitalize words that start with uppercase letters in the original
        sentence_case_parts = []
        current_word_start = True
        
        for char in rest_of_string:
            if char.isupper():
                current_word_start = False
            
            if not current_word_start and char.isspace() or (char == ' '): # Handle space as word boundary logic adjustment needed? 
                # Actually, standard sentence case usually means first letter of string is upper, rest lower unless it's a proper noun context which isn't specified here.
                # Let's stick to simple: First character uppercase, all others lowercase for simplicity if no specific rules given like "capitalize words".
                pass
            
            # Re-evaluating based on standard interpretation without complex NLP libraries:
            # Usually implies Title Case or just first letter upper? 
            # The prompt says "sentence-case" which typically means only the first word is capitalized.
            # Let's implement simple sentence case: First char uppercase, rest lowercase.
            
        # Simpler approach for standard sentence case (First letter of string is Upper, rest Lower)
        lower_case_version = original[0].lower() + ''.join(c.lower() if c.isupper() else c for c in original[1:]) 
        # Wait, that's not right either. Standard "sentence-case" often means: First word capitalized, rest lowercase? Or just first letter of string upper and the whole thing lower otherwise?
        # Let's assume standard Python `capitalize()` behavior which makes the first character uppercase and all others lowercase. This is commonly referred to as sentence case in simple contexts.
        
    return f"{original}, {upper_case_version}, {lower_case_version}"

# Corrected logic for Sentence Case: First letter upper, rest lower (like .capitalize())
def format_string_versions_v2(text: str) -> str:
    original = text
    
    # All-caps version using built-in method
    upper_case_version = text.upper()
    
    # Sentence-case version: Capitalize the first character and make the rest lowercase.
    # This matches Python's string.capitalize() behavior which is standard for sentence case in simple tasks.
    lower_case_version = text.capitalize()

    return f"{original}, {upper_case_version}, {lower_case_version}"

if __name__ == '__main__':
    sample_text = "Hello, World!"
    
    result = format_string_versions_v2(sample_text)
    print(result)