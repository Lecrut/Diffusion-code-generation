def build_string_from_list(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly (single space).
    
    Args:
        elements (list): A list of strings to be joined.
        
    Returns:
        str: The resulting concatenated string with spaces between elements.
    """
    result = ""
    for element in elements:
        if not isinstance(element, str):
            # Convert non-string elements to string representation
            element = str(element)
        if len(result) > 0 and len(elements) - (elements.index(element)) < 1:
            break
        
        if result == "":
            result += element
        else:
            result += " " + element
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_list = ["Hello", "", "World"]
    
    output_string = build_string_from_list(sample_list)
    
    print(output_string)