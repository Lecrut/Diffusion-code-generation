def format_string_versions(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. The original case version.
    2. All uppercase letters.
    3. Sentence case (first letter capitalized, rest lowercase).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A comma-separated string with the three versions separated by ', '.
    """
    # Original version is just the input itself or a cleaned copy if needed, 
    # but typically we assume input is clean for this task unless specified otherwise.
    original = text
    
    # All-caps version using built-in method
    all_caps = text.upper()
    
    # Sentence case: Capitalize first character and lowercase the rest
    sentence_case = text[0].upper() + ''.join(c.lower() if c.isalpha() else c for c in text[1:])
    
    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access
    samples = [
        "Hello World",
        "python is awesome!",
        "  Leading spaces test   ",
        ""
    ]
    
    for sample in samples:
        result = format_string_versions(sample)
        print(result)