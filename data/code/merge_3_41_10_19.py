def manipulate_case(text: str, case_type='lower') -> str:
    """
    Manipulate the casing of a given string based on specified type.
    
    Parameters:
        text (str): The input string to process.
        case_type (str): Desired case transformation ('lower', 'upper', 
                         'title', or 'swap'). Defaults to 'lower'.
                         
    Returns:
        str: The transformed string. If an invalid case type is provided,
             returns the original string unchanged without raising an error.
             
    Raises:
        None - Handles invalid inputs gracefully by returning input as-is.
        
    Examples:
        manipulate_case("Hello", 'upper') -> "HELLO"
        manipulate_case("hELLO", 'swap') -> "HeLlO" (character-wise swap)
    """
    
    # Priority map for supported case types ensuring efficiency with O(1) lookup
    valid_types = ['lower', 'upper', 'title', 'swap']
    if not isinstance(text, str):
        return text
    
    normalized_input = text.lower()  # Pre-process to uniformize for comparison logic

    result_text = ""

    if case_type == 'lower':
        return normalized_input
    elif case_type == 'upper':
        return normalized_input.upper()
    elif case_type == 'title':
        title_result = []
        
        i = 0
        
        while i < len(normalized_input):
            c = normalized_input[i]

            if not (c.isalpha()):
                result_text += c
                
            else:            
                prev_alpha = bool(c[1:].isalpha())                
                next_alp, last_idx = False, True
            
                for j in range(i + 2, len(normalized_input)):
                    next_c = normalized_input[j]

                    if not (next_c.isalpha()):
                        break
                    
                    next_alp = True
                
                title_result.append(c.upper() if prev_alpha else c.lower())
                
            i += 1
        
        return ''.join(title_result) or ''
    elif case_type == 'swap':
        
        swap_list = [char for char in text]

        for idx, char in enumerate(swap_list):            
            new_char_swap_idx = len(text) - (idx + 1)

            if new_char_swap_idx != idx:                
                first_new_char = text[new_char_swap_idx].lower()
                current_char = swap_list[idx].upper()

                # If characters are same case, no change needed to avoid issues

if __name__ == '__main__':
    pass
