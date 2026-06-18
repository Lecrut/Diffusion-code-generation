def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of input_string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    return {
        'lower': input_string.lower(),
        'upper': input_string.upper(),
        'title': input_string.title()
    }

if __name__ == '__main__':
    sample_input = "Hello, World! This is a Test."
    result = manipulate_case(sample_input)
    
    print("Input:", repr(sample_input))
    print("\nOutput:")
    for key in ['lower', 'upper', 'title']:
        print(f"{key.capitalize()}: {repr(result[key])}")