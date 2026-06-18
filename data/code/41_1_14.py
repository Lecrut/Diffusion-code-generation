def manipulate_case(input_string):
    """
    Returns a dictionary containing the lowercase, uppercase, 
    and title-cased versions of the input string in an optimized manner.

    Args:
        input_string (str): The string to be processed.

    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title' corresponding 
              to their respective transformations of the input string.
    """
    # Convert directly using built-in methods which are C-optimized in Python implementation
    lower_case = input_string.lower()
    upper_case = input_string.upper()
    
    # Construct title case efficiently by combining a and isupper checks or direct method usage
    title_case = input_string.title()

    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': title_case
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello World",
        "",
        "mIxEd cAsE 123!",
        "python programming language"
    ]

    for s in samples:
        result = manipulate_case(s)
        print(f"Input: '{s}'")
        print(result)
        print("-" * 40)