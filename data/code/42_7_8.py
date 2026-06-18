def join_strings_with_delimiter(string_list: list[str], delimiter: str) -> str:
    """
    Returns a single string with elements from the input list joined by the custom delimiter.
    
    Args:
        string_list (list): A list of strings to be joined.
        delimiter (str): The string used as separator between each element.
        
    Returns:
        str: A new string where delimiters are placed between every original element.
    """
    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without any user input or files.
    test_data = ["apple", "banana", "cherry"]
    custom_separator = ", "
    
    result = join_strings_with_delimiter(test_data, custom_separator)
    print(result)