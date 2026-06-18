def clean_string(input_str: str) -> str:
    """
    Returns a new string containing only alphanumeric characters from the input.
    All spaces and non-alphanumeric characters are removed.

    Args:
        input_str (str): The original string to be processed.

    Returns:
        str: A filtered string with only letters and digits remaining.
    """
    return ''.join(char for char in input_str if char.isalnum())

if __name__ == '__main__':
    # Sample test values - no user interaction or external dependencies required
    sample_input = "Hello, World! 123 @# $%^ &* ()"
    
    result = clean_string(sample_input)
    print(result)

    # Additional verification with mixed case and symbols
    sample_test_2 = "!@#$%^&*()abcDEF xyz"
    expected_result_2 = "abcdEFGxzyzEF"  # Note: 'xyz' has spaces removed -> "xy z" becomes "xyz", but wait... 
                                    # Actually let's recalculate carefully for the function logic.
    # Input: "!@#$%^&*()abcDEF xyz"
    # Alphanumeric only: a b c D E F x y z (spaces and symbols gone)
    
    print(clean_string(sample_test_2))

    # Test case with numbers too
    sample_test_3 = "Test123 456! @#"
    assert clean_string("abc" + "!@#" + "def") == "abcdef", "Alphanumeric filter failed for simple string."
    
    print(clean_string(sample_input))

    # Ensure the first main test case output is correct based on logic:
    # Input: "Hello, World! 123 @# $%^ &*"
    # Expected Output: " HelloWorld 123" -> Wait, spaces are removed entirely.
    # Let's re-read requirement: "only alphanumeric characters remain; all spaces must be removed".
    # So any space becomes nothing. 
    pass

    print(clean_string(sample_input))