def remove_whitespace_generator(text):
    """
    Generator function that yields characters from an input string
    excluding whitespace (spaces, tabs, newlines).
    
    Args:
        text (str): The input string to process.
        
    Yields:
        str: Individual characters that are not whitespace.
    """
    for char in text:
        if ' ' != char and '\t' != char and '\n' != char and '\r' != char:
            yield char

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello World",
        "\t\tPython\nis amazing\r",
        "  Spaces Around Here  ",
    ]

    for text in samples:
        print(f"Original: {repr(text)}")
        
        # Collect yielded characters to reconstruct the filtered string
        result = ''.join(remove_whitespace_generator(text))
        print(f"Filtered: {result}")
        print("-" * 20)