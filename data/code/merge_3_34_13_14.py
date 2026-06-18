import re

def capitalize_first_letter_only(text: str) -> str:
    """
    Processes a block of text to apply the rule where exactly one letter 
    at the beginning of each word is capitalized, preserving all other casing 
    within that specific first-letter position. This includes handling multiple 
    words in a single line and maintaining spaces between them.

    The logic identifies sequences of alphabetic characters (words) and ensures
    only the very first character of such sequence becomes uppercase while 
    leaving subsequent letters unchanged, even if they were originally lowercase or uppercase.
    
    Args:
        text (str): A string containing one or more sentences/paragraphs to process.

    Returns:
        str: The processed string with exactly one capital letter at the start of each word.
    """
    # Use regex to find all words consisting of alphabetic characters
    # \b matches word boundaries, [a-zA-Z]+ captures sequences of letters
    pattern = r'\b([a-zA-Z][a-z]*)\b'

    def replace_match(match):
        original_word = match.group(0)
        if not original_word:  # Safety check for empty strings
            return ""
        
        first_char = original_word[0]
        rest_of_word = original_word[1:]
        
        # Capitalize the first letter only, keep the rest exactly as is (lowercase or mixed)
        capitalized_first = first_char.upper() if not first_char.isupper() else first_char
        
        return f"{capitalized_first}{rest_of_word}"

    result = re.sub(pattern, replace_match, text)
    
    # Ensure that non-alphabetic characters at the start of a word (like numbers or symbols 
    # immediately following spaces) are handled correctly by not modifying them. The regex above handles this naturally.
    return result

if __name__ == '__main__':
    sample_text = "hello world! HELLO WORLD 123 python is awesome."
    
    processed_output = capitalize_first_letter_only(sample_text)
    
    print("Original text:")
    print(sample_text)
    print("\nProcessed text (capitalize first letter only):")
    print(processed_output)