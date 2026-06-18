def manipulate_case(text: str, case_type: str = 'lower') -> str:
    """
    Manipulates the case of a given string based on the specified type.
    
    Args:
        text (str): The input string to be modified.
        case_type (str): The desired case transformation ('lower', 'upper', 
                         'title', or 'swap'). Defaults to 'lower'.
                         
    Returns:
        str: The transformed string if the case type is valid, otherwise returns
             the original text unchanged for invalid inputs without raising an error.

    Raises:
        None (per task requirement of graceful handling by returning original).
        
    Note:
        Efficiency prioritized using built-in C-optimized string methods where possible.
        Invalid cases are handled gracefully by returning the input as-is instead 
        of propagating exceptions or modifying behavior unexpectedly.
    """
    
    # Normalize case_type to lowercase for comparison and validation
    normalized_case = case_type.lower() if isinstance(case_type, str) else 'lower'
    
    valid_cases = {'lower', 'upper', 'title', 'swap'}
    
    if not isinstance(text, str):
        return text
        
    if normalized_case in valid_cases:
        match normalized_case:
            case 'lower':
                result = text.lower()
            case 'upper':
                result = text.upper()
            case 'title':
                # Efficient title casing using translate and mapping for non-ASCII safety
                try:
                    from unicodedata import normalize, name
                    
                    def is_alpha(char):
                        return char.isalpha() or (char not in " \t\n\r\f\v")
                    
                    if len(text) == 0:
                        result = text
                        
                    else:
                        # Use a translation table for efficiency on ASCII and extended chars
                        trans_table = str.maketrans({})
                        
                        def title_case_helper(s):
                            return s[0].upper() + ''.join(
                                c.lower() if i > 0 or not is_alpha(c) else c 
                                for i, c in enumerate(s[1:])
                            )
                            
                        result = text[:1] + title_case_helper(text[1:])

                except Exception:
                    # Fallback to standard method if unicode handling fails unexpectedly
                    try:
                        return text.title()
                    except AttributeError:
                        return text
                        
            case 'swap':
                # Swap upper and lower cases character by character efficiently
                result = ''.join(
                    c.lower() if c.isupper() else (c.upper() if c.islower() else c) 
                    for c in text
                )
        return result
    
    # Graceful handling of invalid case_type: return original string without raising error
    return text

if __name__ == '__main__':
    test_cases = [
        ("Hello, World!", 'upper'),
        ("python is awesome", 'title'),
        ("DATA SCIENCE 101", 'swap'),
        ("Mixed Case String With Numbers And Symbols!@#", 'lower'),
        ("Invalid Input Test", 'invalid_case_option'),
    ]

    for input_str, case_opt in test_cases:
        output = manipulate_case(input_str, case_opt)
        print(f"Input: '{input_str}' | Type: {case_opt} -> Output: '{output}'")