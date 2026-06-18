def concatenate_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.
    
    Args:
        string_list (list): A list containing the strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".
        
    Returns:
        str: The resulting concatenated string.
    """
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise TypeError("Input must be a non-empty list of strings.")
    
    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or external dependencies are used.
    sample_strings = ["Hello", "World", "This", "Is", "Python"]
    custom_delimiter = " | "

    result_string = concatenate_strings(sample_strings, custom_delimiter)
    
    print(result_string)