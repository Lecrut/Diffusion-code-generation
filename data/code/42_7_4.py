def join_with_delimiter(string_list: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with the given custom delimiter placed between elements.
    
    Args:
        string_list (list): A list of strings to be joined.
        delimiter (str): The string separator to insert between items.
        
    Returns:
        str: A single string with delimiters inserted between original elements.
    """
    if not string_list:
        return ""
    
    result = []
    for i in range(len(string_list)):
        if i > 0 and i < len(string_list):
            # Add delimiter before current element (except the last one)
            result.append(delimiter + string_list[i])
        else:
            result.append(string_list[i])
    
    return "".join(result)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_delim = "-PLUS-"
    
    output_string = join_with_delimiter(sample_strings, custom_delim)
    print(output_string)