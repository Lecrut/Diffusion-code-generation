def remove_whitespace_generator(text: str):
    """
    A generator function that yields characters from an input string,
    skipping any whitespace (spaces, tabs, newlines).
    
    Args:
        text (str): The input string to process.
        
    Yields:
        str: Individual non-whitespace characters one at a time.
    """
    for char in text:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    sample_strings = [
        "Hello World",
        "\tPython\tis\namazing\r",
        "   Leading spaces  ",
        ""
    ]

    for test_input in sample_strings:
        print(f"Input: {repr(test_input)}")
        result = ''.join(remove_whitespace_generator(test_input))
        print(f"Output: '{result}'\n")