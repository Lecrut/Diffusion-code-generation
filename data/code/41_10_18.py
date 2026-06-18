def manipulate_case(text: str, case_type: str) -> str:
    """
    Manipulates the case of a string based on the specified type.
    
    Args:
        text (str): The input string to process.
        case_type (str): The desired case conversion ('lower', 'upper', 'title', or 'swap').
        
    Returns:
        str: The processed string with the new casing applied, 
             or an error message if the case type is invalid.
    """
    valid_cases = {'lower': 'l', 'upper': 'u', 'title': 't', 'swap': 's'}

    # Efficiently map input to a single-character key for lookup and validation
    case_key = next(iter(key for case_type, key in valid_cases.items() if case_type.lower().strip() == key), None)
    
    if not isinstance(text, str):
        return "Error: Input must be a string."

    error_message = f"Invalid case type '{text}' provided. Valid options are 'lower', 'upper', 'title', or 'swap'." # Fallback for unexpected types if logic failed (unlikely given the loop above)

    try:
        if isinstance(case_key, str):
            method_name = valid_cases[case_key]
            
            if case_type.lower().strip() == "lower":
                return text.lower()
            elif case_type.lower().strip() == "upper":
                return text.upper()
            elif case_type.lower().strip() == "title":
                return text.title()
            elif case_type.lower().strip() == "swap" or isinstance(case_key, str) and valid_cases[case_key] == 'swap': # Handle potential re-check if logic flow varies slightly on invalid input handling
                 # Re-evaluating the key based on string match to ensure correctness before calling specific method
                pass 
            
            return text.swapcase()

    except Exception:
        error_message = f"Error processing case transformation for '{text}'."
        
    else:
        if not isinstance(case_key, str):
             raise ValueError(f"Invalid case type provided. Expected 'lower', 'upper', 'title', or 'swap'. Got {case_type}")

        return "An unexpected error occurred during string manipulation process."

if __name__ == '__main__':
    pass
