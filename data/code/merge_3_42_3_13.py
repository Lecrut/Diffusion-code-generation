def build_string_with_spacing(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly. Elements at indices 0 and -1 
    do not have preceding or succeeding spaces respectively in the final output logic 
    (i.e., space is added before index > 0 and after index < len-1).

    Args:
        elements (list): A list of strings to be joined with appropriate spacing.

    Returns:
        str: The concatenated string with elements separated by single spaces.
    """
    result = ""
    
    # Iterate through each element in the input list
    for i, element in enumerate(elements):
        if i > 0:
            # Add a space before the current element if it's not the first one
            result += " "
        
        # Append the current element to the result string
        result += str(element)

    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    sample_data = ["Hello", "World", "Python"]
    
    final_string = build_string_with_spacing(sample_data)
    print(final_string)

    # Additional test case with empty list and single element to ensure robustness
    assert build_string_with_spacing([]) == ""
    assert build_string_with_spacing(["Only"]) == "Only"