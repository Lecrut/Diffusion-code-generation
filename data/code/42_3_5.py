import sys

def build_string_from_list(elements: list[str]) -> str:
    """
    Iteratively builds a string by appending each element from the input list,
    managing spacing between elements correctly. Elements in the list are joined 
    with two spaces ('  ') and no trailing space is added at the end of the result.

    Args:
        elements (list[str]): A list of strings to be concatenated into a single string.

    Returns:
        str: The resulting concatenated string with double spaces between elements.
    
    Example:
        >>> build_string_from_list(['Hello', 'world'])
        'Hello  world'
    """
    result = ""
    # Iterate over each element in the list, appending it to the current separator state
    for i, item in enumerate(elements):
        if i > 0:
            # If this is not the first element, append two spaces before adding the new element
            result += "  "
        
        # Append the current string element
        result += item
    
    return result

if __name__ == '__main__':
    sample_list = ["This", "is a ", "test"]
    
    final_output = build_string_from_list(sample_list)
    
    print(final_output)