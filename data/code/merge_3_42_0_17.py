def concatenate_strings(string_list: list, delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        string_list (list): A list containing items to be joined as strings.
        delimiter (str): The string used to separate the original elements in the final result.

    Returns:
        str: The concatenated string with delimiters between elements.
    
    Raises:
        TypeError: If any element in the input list is not a string instance, 
                  or if the input itself is not a list of strings (including empty lists).
    """
    # Validate that all elements are actually strings to ensure robustness against mixed types
    for item in string_list:
        if not isinstance(item, str):
            raise TypeError(f"Expected only strings in the list. Found non-string element: {type(item)}")

    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    sample_input = ["Hello", "World", "Python"]
    sample_delimiter = "- "
    
    result_string = concatenate_strings(sample_input, sample_delimiter)
    print(f"Concatenated Result: '{result_string}'")

    # Additional test case with different delimiter and empty string element
    edge_case_input = ["Start", "", "End"]
    edge_case_result = concatenate_strings(edge_case_input, "; ")
    
    if isinstance(result_string, str) and result_string == f"{sample_delimiter.join(sample_input)}":
        print("Basic test passed.")
    else:
        raise AssertionError(f"Basic concatenation failed. Expected '{f'{delim}-join'}', got '{result_string}'")

    # Verify edge case handling for empty strings within the list
    if isinstance(edge_case_result, str) and len(edge_case_result) > 0:
        print("Edge case with empty string handled correctly.")
    else:
        raise AssertionError(f"Edge case test failed. Got '{edge_case_result}'")

    # Test TypeError behavior for non-string inputs (optional check logic here just to show robustness, 
    # though the function itself raises it before returning)
    try:
        bad_input = ["Valid", 123]
        concatenate_strings(bad_input, ", ")
    except TypeError as e:
        if "non-string element" in str(e):
            print("Non-string input validation works correctly.")
        else:
            raise AssertionError(f"Unexpected error message for non-string check: {e}") from None

    # Final confirmation of module execution success
    print("All internal tests completed successfully.")