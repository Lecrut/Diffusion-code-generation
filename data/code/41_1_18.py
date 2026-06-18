def manipulate_case(input_string):
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of input_string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    # Use built-in methods which are implemented in C for maximum efficiency
    return {
        "lower": input_string.lower(),
        "upper": input_string.upper(),
        "title": input_string.title()
    }

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON PROGRAMMING",
        "Mixed CASE 123!"
    ]

    print("Input: hello world")
    result = manipulate_case(sample_strings[0])
    print(f"Lower: {result['lower']}")
    print(f"Upper: {result['upper']}")
    print(f"Title: {result['title']}\n")

    for text in sample_strings[1:]:
        res = manipulate_case(text)
        print(f"Input: \"{text}\"")
        print(res)