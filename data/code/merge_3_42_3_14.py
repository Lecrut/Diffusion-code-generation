def build_string_with_spacing(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly.
    
    If the list is empty, returns an empty string.
    Otherwise, joins elements with a single space separator.

    Args:
        elements (list): A list of strings to be joined into a result string.

    Returns:
        str: The resulting concatenated string with spaces between elements.
    """
    if not elements:
        return ""
    
    # Initialize the first element as the start of our result
    result = elements[0]
    
    # Iterate over the remaining elements starting from index 1
    for i in range(1, len(elements)):
        current_element = elements[i]
        
        # Append a space before each subsequent element to ensure correct spacing
        result += " " + current_element
        
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_list = ["Hello", "World", "This", "Is", "An"]
    
    final_string = build_string_with_spacing(sample_list)
    
    print(final_string)

# Expected Output: Hello World This Is An