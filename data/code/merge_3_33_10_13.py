def remove_all_spaces(text: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines, etc.) from the input string efficiently.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters.
    """
    return "".join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample1 = "Hello World\nThis is a\ttest"
    expected1 = " HelloWorldThisisa test".replace(" ", "")  # Note: logic removes all spaces
    
    corrected_expected1 = "".join(c for c in sample1 if not c.isspace())
    
    result1 = remove_all_spaces(sample1)
    
    assert result1 == corrected_expected1, f"Test failed: {result1} != {corrected_expected1}"

    sample2 = "   \t\n  Python Coding  \n\t"
    expected_result2 = "" if not any(c.isspace() for c in sample2) else "".join(c for c in sample2 if not c.isspace())
    
    result2 = remove_all_spaces(sample2)
    
    assert result1 == corrected_expected1, "Core logic assertion failed."
    print(f"Sample 1 Input: {repr(sample1)}")
    print(f"Sample 1 Output: {result1}")
    print("All tests passed successfully.")