def build_string_from_list(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly (single space).
    
    Args:
        elements (list[str]): List of strings to be concatenated.
        
    Returns:
        str: The resulting joined string with spaces between elements.
    """
    result = ""
    for element in elements:
        if len(result) > 0 and not result.endswith(" "):
            result += " "
        result += element
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = ["Hello", "World", "This", "Is", "A", "Test"]
    
    final_string = build_string_from_list(sample_data)
    
    print(final_string)