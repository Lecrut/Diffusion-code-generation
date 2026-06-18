def manipulate_case(input_string):
    """
    Accepts a string and returns a dictionary containing:
    - 'lower': The lowercase version of the input string.
    - 'upper': The uppercase version of the input string.
    - 'title': The title-cased version of the input string (first character 
      capitalized for each word).

    This implementation uses built-in string methods which are implemented in C
    and offer maximum efficiency compared to manual iteration or regex-based approaches.

    Args:
        input_string (str): The original string to process.

    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    
    Examples:
        >>> manipulate_case("Hello World")
        {'lower': 'hello world', 'upper': 'HELLO WORLD', 'title': 'Hello World'}
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string type, got {type(input_string).__name__}")

    return {
        "lower": input_string.lower(),
        "upper": input_string.upper(),
        "title": input_string.title()
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    samples = ["Hello World", "", "PYTHON IS FUN"]

    for test_input in samples:
        result = manipulate_case(test_input)
        print(f"Input: '{test_input}'")
        print("Result:", result)
        print("-" * 40)