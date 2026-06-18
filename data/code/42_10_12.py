def build_string_from_parts(parts: list[str], separator: str = "") -> str:
    """
    Concatenates a list of strings into a single string with an optional separator.

    Args:
        parts (list[str]): A list of strings to be concatenated.
        separator (str, optional): The string to insert between elements in the list.
                                  Defaults to empty string.

    Returns:
        str: The resulting concatenated string.
    
    Handles edge cases such as an empty input list by returning a single empty string.
    """
    if not parts:
        return ""
    
    result = []
    for i, part in enumerate(parts):
        result.append(part)
        # Append separator only if there is another element following the current one
        if i < len(parts) - 1:
            result.append(separator)
    
    return "".join(result)

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    sample_list_1 = ["Hello", "World"]
    separator_1 = ", "
    output_1 = build_string_from_parts(sample_list_1, separator_1)

    sample_list_2 = []
    separator_2 = "-"
    output_2 = build_string_from_parts(sample_list_2, separator_2)

    sample_list_3 = ["Python", ", ", "is"]
    separator_3 = ""
    output_3 = build_string_from_parts(sample_list_3, separator_3)

    print(f"Test 1: {output_1}")
    print(f"Test 2 (empty list): '{output_2}'")
    print(f"Test 3: {output_3}")