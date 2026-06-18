import sys

def process_string(text):
    """Process a string to return three variations: original, all caps, and title case."""
    # Original string (preserving input as-is)
    original = text
    
    # Fully capitalized string using str.upper()
    fully_capitalized = text.upper()
    
    # String with first letter of every word capitalized using str.title()
    # Note: str.title() capitalizes the first character of each word, but may have edge cases 
    # (e.g., converting 'lowercase' to 'LowerCase'). For standard use, it is appropriate.
    title_case = text.title()
    
    return original, fully_capitalized, title_case

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user input, command-line arguments, or network access used here.
    sample_input = "hello world"

    result_original, result_full_upper, result_title_lower = process_string(sample_input)

    print(result_original)
    print(result_full_upper)
    print(result_title_lower)