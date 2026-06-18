def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title' mapping their respective transformed strings.
    """
    # Compute transformations efficiently using built-in methods which are C-optimized in Python
    return {
        'lower': input_string.lower(),
        'upper': input_string.upper(),
        'title': input_string.title()
    }

if __name__ == '__main__':
    sample_input = "Hello, World! This is a TEST."
    
    # Process the hard-coded sample value
    result = manipulate_case(sample_input)
    
    # Print the results to verify functionality (no interactive prompts used)
    print("Input:", repr(sample_input))
    print("Lowercase:", result['lower'])
    print("Uppercase:", result['upper'])
    print("Title Case:", result['title'])