def minify_text(input_string: str) -> str:
    """
    Strips all forms of whitespace from the input string.

    Args:
        input_string (str): The original text containing various whitespace characters.

    Returns:
        str: A new string with no leading, trailing, or internal whitespaces.
    
    Complexity Analysis:
        Time: O(n) where n is the length of the input string. Iterates through once to build a list 
              and then joins it in another pass (or via one-pass join if optimized). Using 'join' 
              after filtering is generally faster than repeated concatenation due to Python's C-implementation optimization,
              but for pure speed without external libraries, we can use a generator expression with ''.join().

        Space: O(n) - To store the new string result. A temporary list of characters or direct joining avoids extra large lists 
                if memory is constrained, though n space is needed regardless to hold output data.
    """
    return "".join(char for char in input_string if not (" " <= ord(char) < 33))

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user interaction or file access
    test_cases = [
        "\t\n\r   Hello, World! \t\n\r",     # Mixed leading/trailing whitespace and tabs/carriage returns
        "  Python3.9\tis awesome...  ",      # Spaces and tabs mixed in the middle with trailing space
        "...!!! ... !!!...",                  # String without any actual whitespaces (edge case)
        "",                                   # Empty string
    ]

    for test_input in test_cases:
        result = minify_text(test_input)
        print(f"Input: {repr(test_input)}")
        print(f"Output: {repr(result)}\n")