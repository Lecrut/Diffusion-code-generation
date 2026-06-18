def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        strings (list): A list of string elements to be joined.
        delimiter (str): The string to use as the separator between elements.
        
    Returns:
        str: A single string where delimiters are placed between each element.
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
    for i in range(len(strings)):
        result.append(strings[i])
        # Append delimiter after the current element, except for the last one
        if i < len(strings) - 1:
            result.append(delimiter)
            
    return "".join(result)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    output_string = join_strings_with_delimiter(sample_list, custom_delim)
    print(output_string)