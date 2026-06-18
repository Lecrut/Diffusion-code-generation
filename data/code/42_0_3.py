def concatenate_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        string_list (list[str]): A list containing the strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".

    Returns:
        str: The resulting concatenated string.
    
    Raises:
        TypeError: If any item in the input list is not a string or if the input itself is not a list of strings.
    """
    # Validate that all elements are actually strings before joining
    for i, item in enumerate(string_list):
        if not isinstance(item, str):
            raise TypeError(f"Element at index {i} must be a string, got {type(item).__name__}")

    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or CLI args needed)
    sample_strings = ["Hello", "World", "This", "Is", "A"]
    custom_delimiter = "-+"

    result_string = concatenate_strings(sample_strings, custom_delimiter)
    
    print(f"Input List: {sample_strings}")
    print(f"Delimiter used: '{custom_delimiter}'")
    print("Concatenated Result:")
    print(result_string)