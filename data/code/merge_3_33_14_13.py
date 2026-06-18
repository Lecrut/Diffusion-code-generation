def minify_text(input_string: str) -> str:
    """
    Removes all forms of whitespace from the input string efficiently.
    
    Args:
        input_string (str): The string to process.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_inputs = [
        "Hello, World!   ",
        "\t\n  Multiple lines of whitespace\r",
        "NoWhitespaceHere123",
        " Mixed   Spans \t\t And Newlines\n"
    ]

    for test_input in sample_inputs:
        result = minify_text(test_input)
        print(f'Input: {repr(test_input)}')
        print(f'Result: {result}')