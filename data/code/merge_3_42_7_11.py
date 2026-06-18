def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        strings (list[str]): A list of string elements to be joined.
        delimiter (str): The string used as the separator between elements.
        
    Returns:
        str: A single string where delimiters are inserted between each element.
             If the input list is empty, returns an empty string.
    
    Example:
        >>> join_strings_with_delimiter(["a", "b"], ",")
        'a,b'
        >>> join_strings_with_delimiter([], "-")
        ''
    """
    if not strings:
        return ""
    
    result = []
    for i, item in enumerate(strings):
        # Append the current string and its delimiter (except after the last element)
        result.append(item + delimiter)
    
    # Remove the trailing delimiter added by the loop logic above
    if len(result) > 0:
        return "".join(result[:-1])
    else:
        return ""

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    output_string = join_strings_with_delimiter(sample_list, custom_delim)
    print(output_string)