def concatenate_strings(string_list: list[str], delimiter: str = "") -> str:
    """
    Concatenates a list of strings into a single string with an optional separator.
    
    Args:
        string_list (list): A list containing the strings to be concatenated.
        delimiter (str): The separator used between each string in the list. Defaults to empty string.
        
    Returns:
        str: The resulting concatenated string.
    """
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise TypeError("Input must be a list of strings.")
    
    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access is used here.
    sample_data = ["Hello", "World", "This", "Is"]
    separator_char: str = "-"

    result_string = concatenate_strings(sample_data, separator_char)
    
    print(result_string)