def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title' mapping to their respective transformed strings.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Efficiently generate all three cases in one pass over the characters for consistency, 
    # though Python's built-in methods are already highly optimized (C-level).
    
    lower_case = input_string.lower()
    upper_case = input_string.upper()
    title_case = input_string.title()

    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': title_case
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello World",
        "python programming is fun!",
        "",
        "   Leading and Trailing Spaces  ",
        "Mixed CASE 123"
    ]

    for test_input in samples:
        result = manipulate_case(test_input)
        print(f"Input: '{test_input}'")
        print(result)
        print("-" * 40)