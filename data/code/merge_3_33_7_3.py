def filter_non_whitespace(iterable):
    """
    Generator function that yields characters from an input string 
    only if they are not whitespace.
    
    Args:
        iterable (str | Sequence[str]): Input sequence of strings or chars.
        
    Yields:
        str: Characters that are not whitespace.
    """
    for char in iterable:
        # Consider any character with a zero width from string.whitespace
        if char != ' \t\n\r\f\v\x0b':
            yield char

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    
    result_string = "".join(filter_non_whitespace(sample_input))
    print(f"Original: {sample_input}")
    print("Filtered:", result_string)

# Additional verification with edge cases if needed for standalone testing without CLI args
def verify_edge_cases():
    """Simple internal checks to ensure correctness"""
    test1 = "  \t\n\r\f\v   abc\ndef\t\n"
    expected1 = "abcdef"
    
    result_str1 = "".join(filter_non_whitespace(test1))
    assert result_str1 == expected1, f"Test failed: {result_str1} != {expected1}"

    test2 = ""
    assert list(filter_non_whitespace(test2)) == []

    print("All internal edge case verifications passed.")