def build_string_from_parts(parts: list[str], separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator between each element.
    
    Args:
        parts (list[str]): A list of string elements to concatenate.
        separator (str): An optional string to insert between elements in the list.
        
    Returns:
        str: The concatenated result as a single string.
        
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements, 
                  and if 'separator' is not a string (though typically handled gracefully).
    
    Note: This function handles empty input lists by returning an empty string immediately.
          It does not perform any network access, file I/O, or require user interaction.
    """
    # Handle the case where parts is None to ensure robustness against unexpected inputs
    if not isinstance(parts, list):
        raise TypeError("The 'parts' argument must be a list.")

    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings. Found {type(item).__name__}.")

    # If the input list is empty, return an empty string regardless of separator
    if len(parts) == 0:
        return ""

    result = parts[0]
    
    # Iterate through the rest of the list and join them with the separator
    for i in range(1, len(parts)):
        result += separator + parts[i]
        
    return result

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input
    
    # Test case 1: Normal concatenation with a comma separator
    sample_list_1 = ["Hello", "World"]
    sep_1 = ", "
    output_1 = build_string_from_parts(sample_list_1, sep_1)
    
    # Test case 2: Empty list handling
    empty_list = []
    output_empty = build_string_from_parts(empty_list)
    
    # Test case 3: Single element with separator (separator should not appear before the first or after last usually, 
    # but logic here appends sep + next item. If only one item, loop doesn't run, so no extra separators added).
    single_item = ["Python"]
    output_single = build_string_from_parts(single_item)
    
    print(f"Test 1 - List: {sample_list_1}, Separator: '{sep_1}'")
    print(f"Result: '{output_1}'\n")
    
    print("Test 2 - Empty List:")
    print(f"Result: '{output_empty}'\n")
    
    print("Test 3 - Single Item:")
    print(f"List: {single_item}")
    print(f"Result: '{output_single}'\n")

    # Additional test with multiple items and different separator
    complex_list = ["Apples", "Bananas", "Cherries"]
    sep_complex = "-and-"
    output_complex = build_string_from_parts(complex_list, sep_complex)
    
    print(f"Test 4 - Complex List: {complex_list}, Separator: '{sep_complex}'")
    print(f"Result: '{output_complex}'")