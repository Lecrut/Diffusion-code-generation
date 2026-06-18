def manipulate_case(text: str, case_type: str = 'lower') -> str:
    """
    Manipulates the case of a given string based on the specified type.
    
    Args:
        text (str): The input string to be manipulated.
        case_type (str): The desired case transformation ('lower', 'upper', 
                         'title', or 'swap'). Defaults to 'lower'.
                         
    Returns:
        str: The transformed string if valid, otherwise the original string.

    Raises:
        ValueError: If an invalid case type is provided.
        
    Note:
        This function prioritizes efficiency by using built-in C-optimized 
        string methods where possible and avoiding unnecessary intermediate objects.
    """
    
    # Define supported cases for clarity and validation without overhead of a large dict lookup on every call
    valid_cases = {'lower', 'upper', 'title', 'swap'}
    
    if case_type not in valid_cases:
        raise ValueError(f"Invalid case type '{case_type}'. Supported types are {valid_cases}")

    # Handle empty string early to avoid unnecessary processing
    if not text:
        return ""

    try:
        if case_type == 'lower':
            result = text.lower()
        elif case_type == 'upper':
            result = text.upper()
        elif case_type == 'title':
            # title() handles non-alphabetic characters well by leaving them as is, 
            # which matches standard expectations for this operation.
            result = text.title()
        elif case_type == 'swap':
            # Swapcase converts all uppercase to lowercase and vice versa.
            result = text.swapcase()
        
        return result
        
    except Exception:
        # Fallback in case of unexpected internal errors, though standard string methods are robust.
        return text

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    test_cases = [
        ("Hello World", 'lower'),
        ("HELLO WORLD", 'upper'),
        ("hello world", 'title'),
        ("HeLLo WoRLd", 'swap'),
        ("  Mixed Case String! ", 'upper'),
        "", 'lower',
    ]

    for input_str, case in test_cases:
        try:
            output = manipulate_case(input_str, case)
            print(f"Input: '{input_str}' | Type: {case} -> Output: '{output}'")
        except ValueError as e:
            print(f"Error processing type '{case}': {e}")

    # Demonstrate error handling for invalid input
    try:
        manipulate_case("Test", "invalid_type")
    except ValueError:
        pass  # Expected behavior, no output needed here other than the exception being caught implicitly by context or printed if desired. 
              # Since we are not printing errors explicitly in this block to keep it clean unless requested, 
              # but for robustness demonstration above we could print. Let's add a specific test for invalid input below:

    try:
        manipulate_case("Sample", "random")
    except ValueError as ve:
        print(f"Caught expected error for invalid case type 'random': {ve}")