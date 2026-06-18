def minify_text(input_string: str) -> str:
    """
    Strips all forms of whitespace from the input string efficiently.
    
    This function iterates through the characters, skipping any that are 
    considered whitespace (spaces, tabs, newlines, etc.), and constructs a 
    result string with only non-whitespace characters concatenated together.

    Args:
        input_string (str): The raw text to process.
        
    Returns:
        str: A new string containing all original characters except whitespace.
    
    Complexity Analysis:
        Time: O(n) where n is the length of the input string, as each character 
              is visited exactly once during iteration and appended if not a space.
        Space: O(m) for storing the result string, where m <= n.

    Examples:
        >>> minify_text("  hello   world\n\t")
        'helloworld'
        
        >>> minify_text("")
        ''
        
        >>> minify_text("No spaces here!")
        'Nospaceshere!'
    """
    result = []
    
    for char in input_string:
        if not char.isspace():
            result.append(char)
            
    return ''.join(result)

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure the module runs 
    # without user interaction, network access, or file dependencies.
    
    sample_1 = "  Hello   World\n\tThis is a test.\r"
    expected_1 = "HelloWorldThisisatest."
    
    sample_2 = ""
    expected_2 = ""
    
    sample_3 = "No spaces here!"
    expected_3 = "Nospaceshere!"
    
    # Execute tests and print results for verification.
    assert minify_text(sample_1) == expected_1, f"Test 1 Failed: {minify_text(sample_1)} != {expected_1}"
    assert minify_text(sample_2) == expected_2, "Test 2 Failed."
    assert minify_text(sample_3) == expected_3, f"Test 3 Failed: {minify_text(sample_3)} != {expected_3}"
    
    print("All sample tests passed successfully.")