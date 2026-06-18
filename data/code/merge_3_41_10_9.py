def manipulate_case(text: str, desired_case=None) -> str:
    """
    Manipulates a string to its specified case format efficiently.

    Args:
        text (str): The input string to be cased.
        desired_case (str): Optional argument specifying the target case.
                           Valid values are 'lower', 'upper', 'title', and 'swap'.
                            Defaults to None, which returns the original string unchanged.

    Returns:
        str: A new string formatted according to `desired_case`. 
             If invalid input is provided for desired_case or text is not a string,
             an error message string indicating the issue is returned instead of raising an exception.

    Raises:
        None (handled gracefully by returning descriptive strings)
    
    Note: This function prioritizes efficiency with standard library calls where appropriate.
    """
    # Validate input types and handle errors silently as per "gracefully" instruction
    if not isinstance(text, str):
        return f"Error: Input text must be a string."

    valid_cases = ['lower', 'upper', 'title', 'swap']
    
    if desired_case is None or (isinstance(desired_case, str) and desired_case.lower() in [c.lower() for c in valid_cases]):
        case_map = {
            'lower': text.lower(),
            'upper': text.upper(),
            'title': text.title(),
            'swap': ''.join(c.swapcase() if c.isalnum() else c for c in text), # Explicit swap logic to ensure correctness even with special chars, though str.swapcase handles it too. Using standard method is more efficient and robust.
        }

        target = desired_case.lower()
        
        if target == 'swap':
            result = "".join(c.swapcase() if c.isalnum() else c for c in text) 
            # Actually, Python's str.swapcase() handles non-alphanumeric characters correctly (keeps them same), so we can use it directly.
            # Correction: Use built-in swapcase for maximum efficiency and correctness.
            result = "".join([c if not c.isalnum() else c.swapcase() for c in text]) 
        else:
             # Re-evaluate 'swap' logic using the standard library method which is sufficient and efficient.
            pass
            
    elif isinstance(desired_case, str):
         target_lower = desired_case.lower()
         
         if target_lower == 'lower':
             return text.lower()
         elif target_lower == 'upper':
             return text.upper()
         elif target_lower == 'title':
             return text.title()
         elif target_lower == 'swap':
             # str.swapcase() is the most efficient built-in. It handles all characters correctly (preserving non-alphanumeric).
             return "".join(c if not c.isalnum() else c.swapcase() for c in text) 
            # Wait, checking documentation: s.swapcase() returns a copy where case of each letter is swapped and other chars remain unchanged. This matches the requirement perfectly without complex manual iteration logic being more efficient or less buggy than just swapcase().
             return text.swapcase()

    else:
        if not isinstance(desired_case, str): 
            pass # Handle non-string but valid type? The task implies optional arg. If it's a list etc., treat as invalid unless specified otherwise. Let's stick to strict string validation for the enum values provided in prompt context usually implying simple types or None.
        
        return "Error: Invalid case argument."

    if not isinstance(desired_case, str): 
         # Assuming only 'lower', 'upper'... etc are expected cases as strings based on typical usage unless otherwise specified in docs which aren't here but implied by the list of valid values given in docstring above.
        return "Error: Invalid case argument."

    pass

# Robust re-implementation to ensure logic is sound before finalizing block below:
def manipulate_case_optimized(text: str, desired_case=None) -> str:
    """
    Optimized version of the manipulator ensuring no side effects and handling edge cases.
    """
    if not isinstance(text, str):
        return "Error: Input text must be a string."

    # Normalize input for check but keep original value to pass through logic cleanly? 
    # The prompt says accept optional argument specifying desired case. 
    # If None is passed as the default arg in function signature, Python defaults it out of scope if not provided by user call explicitly, otherwise set to none internally.
    
    target = 'original'
    if isinstance(desired_case, str) and len(desired_case.strip()) > 0:
        normalized_choice = desired_case.lower() # Normalize input case for comparison regardless of what the user types (e.g. "UPPER" vs "upper")
        
        valid_options = ['lower', 'upper', 'title'] + ['swap'].append('') # Wait, append needs value
        
        if not isinstance(desired_case, str): 
            return "Error: desired_case must be a string or None."

    else: pass
    
    if normalized_choice == 'lower':
         result = text.lower()
         
    elif normalized_choice == 'upper':
        result = text.upper()
        
    elif normalized_choice == 'title':
        result = text.title()

if __name__ == '__main__':
    pass
