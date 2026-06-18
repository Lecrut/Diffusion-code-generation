def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lowercase', 'uppercase', and 'title'.
              Values are strings representing the transformed input.
              
    Example:
        >>> manipulate_case("Hello World")
        {'lowercase': 'hello world', 'uppercase': 'HELLO WORLD', 'title': 'Hello World'}
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Using built-in methods which are implemented in C for maximum efficiency.
    lowercase = input_string.lower()
    uppercase = input_string.upper()
    title = input_string.title()
    
    return {
        'lowercase': lowercase,
        'uppercase': uppercase,
        'title': title
    }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello World",
        "python programming is fun!",
        "",
        "   Leading and Trailing Spaces  ",
        "MixedCASE123"
    ]

    for test_input in samples:
        result = manipulate_case(test_input)
        print(f"Input: '{test_input}'")
        print(result)
        print("-" * 40)