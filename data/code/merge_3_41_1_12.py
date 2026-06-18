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

    # Efficiently generate all three cases in one pass over the characters where possible
    lower = input_string.lower()
    upper = input_string.upper()
    
    # Title case is generally optimized by CPython's built-in method which handles unicode correctly.
    title = input_string.title()

    return {
        'lower': lower,
        'upper': upper,
        'title': title
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello World",
        "python programming is fun!",
        "",
        "123 Main St"
    ]

    for s in samples:
        result = manipulate_case(s)
        print(f"Input: '{s}'")
        print(result)
        print("-" * 40)