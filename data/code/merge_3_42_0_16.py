def concatenate_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        string_list (list): A list containing the strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".

    Returns:
        str: A new string with all elements from the input list joined by the delimiter.
    
    Raises:
        TypeError: If string_list is not a list or contains non-string elements.
    """
    if not isinstance(string_list, list):
        raise TypeError("Input must be a list.")

    for item in string_list:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings, got {type(item).__name__}.")

    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access is used here.
    
    sample_strings = ["Hello", "World", "This", "Is", "Python"]
    custom_delimiter = "-"

    result_string = concatenate_strings(sample_strings, custom_delimiter)

    print(f"Concatenated Result: '{result_string}'")