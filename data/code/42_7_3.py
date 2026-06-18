def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter, returning a single string 
    where the delimiter is placed between every element.
    
    Args:
        strings (list): A list of strings to be joined.
        delimiter (str): The string to use as a separator between elements.
        
    Returns:
        str: The resulting joined string with delimiters inserted between items.
    """
    if not strings:
        return ""
    
    result = strings[0]
    for i in range(1, len(strings)):
        result += delimiter + strings[i]
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    sample_data = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    final_output = join_strings_with_delimiter(sample_data, custom_delim)
    print(final_output)