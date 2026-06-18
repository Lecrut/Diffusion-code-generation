def concatenate_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        string_list (list[str]): A list containing the strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".

    Returns:
        str: The resulting concatenated string.
    
    Raises:
        TypeError: If input is not a list or if elements are not all strings.
    """
    if not isinstance(string_list, list):
        raise TypeError("Input must be a list.")
    
    for item in string_list:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings, got {type(item).__name__}.")

    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access is used here.
    
    sample_strings = ["Hello", "World", "This", "Is", "Python"]
    custom_delimiter = " | "

    result_string = concatenate_strings(sample_strings, custom_delimiter)

    print(result_string)