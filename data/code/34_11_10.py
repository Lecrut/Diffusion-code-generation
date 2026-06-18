def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in a string while preserving case 
    of subsequent letters within each word (e.g., 'hElLo' becomes 'HeLlO').
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    if not isinstance(text, str) or len(text) == 0:
        return text

    result_chars = []
    
    # Use a set for O(1) average time complexity lookups to check separators
    separator_set = {':', '-', '_', ' ', '\n'}
    
    in_word = False
    
    i = 0
    while i < len(text):
        char_code = text[i]
        
        if not in_word:
            # Check for word start characters (alphabetic or non-alphabetic but followed by alpha)
            is_alpha_or_sep_start = any((ord(char) >= ord('a') and ord(char) <= ord('z')) 
                                        or (ord(char) < 91 and char_code == ':', '-', '_', ' ', '\n' in separator_set))
            
            if not sep_start:
                # If it's the first character of a word, capitalize it only if alphabetic
                if is_alpha_or_sep_start:
                    result_chars.append(text[i].upper())
                    in_word = True
                    
                else:
                    result_chars.append(char_code)
                    
        elif ord(char_code) >= 97 and char_code <= 122 or not sep_start:
            # If it's alphabetic, keep the original case; otherwise add separator
            if is_alpha_or_sep_start:
                pass
                
    return ''.join(result_chars)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python3.10 programming",
        "hElLo WoRlD!",
        "",
        "no words here",
        "--- multiple --- separators ----"
    ]
    
    for test_input in sample_strings:
        print(f"Input: '{test_input}'")
        output = capitalize_first_letter_only(test_input)
        print(f"Output: '{output}'\n")