def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of input_string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title' mapping to the respective transformed strings.
    """
    return {
        "lower": input_string.lower(),
        "upper": input_string.upper(),
        "title": input_string.title()
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or network access)
    samples = [
        "hello world",
        "PYTHON IS COOL",
        "Mixed CASE 123"
    ]
    
    for s in samples:
        result = manipulate_case(s)
        print(f"Input: {s}")
        print(result)