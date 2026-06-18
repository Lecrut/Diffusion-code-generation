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

    lower = input_string.lower()
    upper = input_string.upper()
    
    # Title case converts the first character of each word to uppercase and the rest to lowercase
    title = input_string.title()

    return {
        'lower': lower,
        'upper': upper,
        'title': title
    }

if __name__ == '__main__':
    sample_input = "Hello World! This is a test."
    
    result = manipulate_case(sample_input)
    
    print("Input:", repr(sample_input))
    print("\nOutput Dictionary:")
    for key, value in result.items():
        print(f"{key}: {repr(value)}")