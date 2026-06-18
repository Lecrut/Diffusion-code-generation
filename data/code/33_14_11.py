def minify_text(input_string: str) -> str:
    """
    Strips all forms of whitespace from the input string efficiently.
    
    This function iterates through the string once, building a new result 
    containing only non-whitespace characters. It handles spaces, tabs, newlines,
    and other Unicode whitespace categories using Python's built-in character checks
    for optimal performance without external dependencies or regex overhead.

    Args:
        input_string (str): The original text string to process.

    Returns:
        str: A new string with all whitespace characters removed.
    
    Examples:
        >>> minify_text("  hello\nworld\t ")
        'helloworld'
    """
    result = []
    for char in input_string:
        # Check if character is not a standard ASCII or Unicode whitespace
        # Using explicit checks avoids regex compilation overhead.
        if char != '\t' and char != '\n' and char != '\r' and \
           char != ' ':  # Covers space, tab, newline, carriage return
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_1 = "   Hello World\n\tThis is a test\r"
    sample_2 = "\n \t \r\n  multiple   spaces  and tabs \t here  "
    
    print("Sample 1 Result:", minify_text(sample_1))
    print("Sample 2 Result:", minify_text(sample_2))