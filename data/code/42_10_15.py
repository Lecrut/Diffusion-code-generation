def build_string_from_parts(parts: list[str], separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator between each element.

    Args:
        parts (list[str]): A list of string elements to concatenate.
        separator (str): An optional string to insert between elements in the list.

    Returns:
        str: The concatenated result as a single string. If the input list is empty,
             an empty string is returned regardless of the separator provided.
    
    Examples:
        >>> build_string_from_parts(["a", "b"], ", ")
        'a, b'
        >>> build_string_from_parts([], "-")
        ''
        >>> build_string_from_parts(["hello"])
        'hello'
    """
    if not parts:
        return ""

    result = []
    
    # Use a loop to handle separators correctly between elements.
    for i in range(len(parts)):
        if separator and i > 0:
            result.append(separator)
        
        result.append(str(parts[i]))
    
    return "".join(result)

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure the module runs without input.
    
    sample_list_1 = ["apple", "banana", "cherry"]
    separator_1 = ", "
    output_1 = build_string_from_parts(sample_list_1, separator_1)
    print(f"List: {sample_list_1}, Separator: '{separator_1}'")
    print(f"Result: '{output_1}'\n")

    sample_list_2 = ["Python", "is", "great"]
    separator_2 = "-"
    output_2 = build_string_from_parts(sample_list_2, separator_2)
    print(f"List: {sample_list_2}, Separator: '{separator_2}'")
    print(f"Result: '{output_2}'\n")

    sample_list_3 = []
    separator_3 = "|"
    output_3 = build_string_from_parts(sample_list_3, separator_3)
    print(f"List: {sample_list_3}, Separator: '{separator_3}'")
    print(f"Result: '{output_2}'\n") # Note: Logic dictates this should be empty string based on function definition.

    sample_list_4 = ["single"]
    separator_4 = ""
    output_4 = build_string_from_parts(sample_list_4, separator_4)
    print(f"List: {sample_list_4}, Separator: '{separator_4}'")
    print(f"Result: '{output_4}'\n")

    # Additional verification for the empty list edge case specifically mentioned in requirements.
    sample_empty = []
    result_empty = build_string_from_parts(sample_empty)
    assert result_empty == "", "Empty input should return an empty string."
    print("Verification passed: Empty list returns empty string.")