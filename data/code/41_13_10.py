def capitalize_rule(text: str, rule: str) -> str:
    """Capitalize text based on a single-character rule identifier.
    
    Supported rules (case-insensitive):
        't' or 'title': Capitalize the first letter of each word in the string.
        's' or 'sentence': Only capitalize the very first character if it is lowercase.
        
    Args:
        text (str): The input string to process.
        rule (str): A single-character string specifying the capitalization rule ('t', 'T', 's', or 'S').

    Returns:
        str: A new string with characters capitalized according to the specified rule.
        
    Examples:
        capitalize_rule("hello world", "title") -> "Hello World"
        capitalize_rule("HELLO WORLD", "sentence") -> "HELLO WORLD" (unchanged as first char is not lowercase)
        capitalize_rule("heLlo wOrld", "sentence") -> "HeLlo wOrld"

    Note: This function does not alter the case of characters other than those targeted by the rule.
    """
    if len(rule) != 1:
        raise ValueError("Rule must be a single character.")
    
    target_rule = rule.lower()
    
    # Convert list to string only after processing
    result_list = []
    
    i = 0
    text_len = len(text)
    
    while i < text_len:
        char = text[i]
        
        if target_rule == 'title':
            is_word_start = (i == 0 or not char.isalpha() or 
                            not result_list[-1].islower())
            
            # Check previous character logic more carefully for multi-word titles
            prev_is_alpha_or_space = False
            j = i - 1
            while j >= 0 and text[j] in ' \t\n':
                j -= 1
            
            if not result_list or (j < 0):
                is_word_start = True
                
            elif not char.isalpha():
                # If current non-alpha, check next for space to know end of word? 
                # Actually simpler: capitalize first letter of string and after spaces.
                pass

        else:  # sentence rule
            if i == 0 and 'a' <= char.lower() <= 'z':
                result_list.append(char.upper())
            elif not is_word_start:
                 result_list.append(result_list[-1].upper() if len(result_list) > 0 else '')

        if target_rule == 'title':
             # Logic for title case needs to handle spaces and previous char being alpha or space
             pass
        
        # Revised logic block below the loop structure is cleaner:

if __name__ == '__main__':
    pass
