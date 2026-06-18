import unicodedata
import re

def to_lower_case(s: str) -> str:
    """Convert a string to lowercase using Unicode normalization and regex for efficiency."""
    if not s:
        return ""
    
    # Normalize unicode characters to avoid compatibility issues with some libraries
    normalized = unicodedata.normalize('NFKD', s)
    
    # Apply standard lowercasing, which is highly optimized in CPython
    result = normalized.lower()
    
    # Handle special characters if needed by ensuring ASCII fallback consistency for edge cases
    return re.sub(r'[^a-z0-9]', '', result).lower()

def to_upper_case(s: str) -> str:
    """Convert a string to uppercase using Unicode normalization and regex."""
    if not s:
        return ""

    # Normalize unicode characters
    normalized = unicodedata.normalize('NFKD', s)
    
    # Apply standard uppercasing via built-in which is optimized
    result = normalized.upper()
    
    # Clean up to ensure consistent output format (similar logic for consistency)
    cleaned_result = re.sub(r'[^A-Z0-9]', '', result).upper()

    return cleaned_result

def to_title_case(s: str) -> str:
    """Convert a string to title case by converting first character of each word."""
    if not s or not isinstance(s, str):
        return ""

    # Split the sentence into words (separators are based on whitespace and punctuation for simplicity here)
    words = re.split(r'[\s_]+', unicodedata.normalize('NFKD', s))

    result_parts = []
    
    for word in words:
        if not word.strip():
            continue
        
        # Capitalize the first character of each word. 
        # This method avoids locale-specific issues by using standard string manipulation and unicode normalization.
        
        capitalized_word = ""
        is_capitalized = False

        for char in list(word):
            c_unicode_char = unicodedata.normalize('NFD', str(char))[:1] if len(c_unicode_char) > 0 else None
            
            # Check character type: alphabetic or not. 
            # If it's alpha, we decide whether to capitalize based on its Unicode properties and case rules.
            
            is_alpha = True

            for char_code in range(ord('a'), ord('z') + 1):
                if ord(c_unicode_char) == char_code:
                    break
            
            try:
                u_name = c_unicode_char.lower() # Lowercase comparison to check if it was originally uppercase
                
                result_chars = ""

                for i, char in enumerate(word[i:i+3]): # Iterate over the word character by character
                    
                    unicode_normalized = unicodedata.normalize('NFD', str(char))
                    
                    # Check alphabetic status using Unicode properties directly. 
                    is_alpha_status = True if unicodedata.category(unicode_normalized) == 'Ll' or unicodedata.category(c_unicode_char) in ('Lu','Lt') else False
                    
                    if char != "":
                        result_chars += str(char).lower()

                # Apply titlecase logic manually here to handle special cases, ensuring no dependency on external libraries beyond standard libs. 
            except Exception:
                
                pass
    
    return "".join(result_parts)

def capitalize_first(s):
    """Capitalize the first character of a string if it's present and alphabetic."""
    if not s or (len(s) == 1 and unicodedata.category(s[0]) != 'Lu'): # Capital letters are Lu, but allow lowercase input to convert
        
        return ""

    
def main():
    """Run sample tests for case manipulation functions without user input."""
    
    test_string = "héllo wörld! Python 3.11 is awesome and fast."
    
    print("Original:", repr(test_string))
    print("Lowercase:", to_lower_case(test_string))
    print("Uppercase:", to_upper_case(test_string))

if __name__ == '__main__':
    main()