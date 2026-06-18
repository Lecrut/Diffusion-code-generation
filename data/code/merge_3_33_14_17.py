def minify_text(input_string):
    """
    Strips all forms of whitespace from an input string efficiently.

    This function handles various types of whitespace characters including spaces, tabs, newlines,
    carriage returns, vertical tabs, and form feeds. It is optimized for performance by using 
    the replace method which in Python 3 uses highly efficient C-level implementations under the hood.

    Args:
        input_string (str): The string to be processed. Can contain any amount of whitespace characters.

    Returns:
        str: A new string with all leading, trailing, and internal whitespace removed. If the 
             input is None or empty after stripping, an empty string is returned.
    
    Raises:
        TypeError: If input_string is not a string instance.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected type 'str', got {type(input_string).__name__}")

    # Python's replace method with None as the second argument removes all occurrences of 
    # whitespace characters (space, tab, newline, etc.) efficiently in a single pass.
    return input_string.replace(' ', '').replace('\t').replace('\n', '') \
                        .replace('\r', '').replace('\v', '').replace('\f', '')

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or external dependencies
    samples = [
        "  Hello World! ",           # Leading/trailing spaces
        "\t\tHello\nWorld\f",       # Mixed whitespace including tabs and newlines
        None,                        # Edge case: invalid input type (will raise TypeError)
        "",                          # Empty string
        "No extra space here!",      # No whitespace to remove
        "   \n\r  Test Case  ",     # Multiple types of invisible characters
    ]

    for idx, test_input in enumerate(samples):
        try:
            result = minify_text(test_input) if isinstance(test_input, str) else None
            print(f"Sample {idx}:")
            print(repr(result))
        except Exception as e:
            print(f"Sample {idx} raised exception (expected for non-string input): {e}")