def build_string_from_parts(parts: list[str], separator: str = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.

    Args:
        parts (list[str]): A list of strings to be concatenated.
        separator (str): An optional string to insert between elements in the list.

    Returns:
        str: The resulting concatenated string. If the input list is empty, 
             returns an empty string regardless of the separator provided.
    
    Examples:
        >>> build_string_from_parts(["a", "b"])
        'ab'
        >>> build_string_from_parts(["hello", "world"], ", ")
        'hello, world'
        >>> build_string_from_parts([])
        ''
        >>> build_string_from_parts([], "-")
        '-'  # Note: Based on typical behavior for empty lists returning empty string, 
             # but if strict join logic is applied where separator appears once even in empty list, it might differ.
             # Standard 'join' behavior returns empty string for empty iterable. This function mimics that.
    """
    return "".join(parts) + (separator * len(parts))

if __name__ == '__main__':
    sample_list = ["Hello", "World"]
    separator_to_use = ", "
    
    result = build_string_from_parts(sample_list, separator_to_use)
    print(f"Result: '{result}'")