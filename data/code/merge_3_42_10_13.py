def build_string_from_parts(parts: list[str], separator: str = "") -> str:
    """
    Concatenates a list of strings with an optional separator between elements.
    
    Args:
        parts (list[str]): A list of string components to concatenate.
        separator (str): An optional string to insert between each element in the list.
        
    Returns:
        str: The concatenated result as a single string.
        
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    
    Examples:
        >>> build_string_from_parts(["a", "b"])
        'ab'
        >>> build_string_from_parts(["hello", "world"], separator=" ")
        'hello world'
        >>> build_string_from_parts([])
        ''
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")
    
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the input list must be strings. Found {type(item).__name__}.")

    # Using join is efficient and handles empty lists correctly (returns empty string)
    return separator.join(parts)

if __name__ == '__main__':
    sample_list = ["Hello", "World"]
    custom_separator = ", "
    
    result_with_sep = build_string_from_parts(sample_list, custom_separator)
    print(f"Joined with '{custom_separator}': {result_with_sep}")

    empty_result = build_string_from_parts([])
    print(f"Empty list joined: \"{empty_result}\"")

    no_sep_result = build_string_from_parts(["Python", "is", "great"])
    print(f"No separator used: {no_sep_result}")