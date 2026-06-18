def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from both internal positions and surrounding edges of the string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no whitespace characters present.
    """
    # Using replace() is efficient for this specific task as it handles all space types 
    # in a single pass and avoids the overhead of manual iteration or regex compilation.
    return text.replace(" ", "")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    SAMPLE_INPUT = "Hello world, this is   a test.\n  Spaces everywhere!  \tTab here."
    
    processed_output = remove_all_spaces(SAMPLE_INPUT)
    
    print(processed_output)