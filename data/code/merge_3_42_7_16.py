def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        strings (list[str]): A list of string elements to be joined.
        delimiter (str): The string to use as the separator between elements.
        
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
    
    result = [strings[0]]
    for i in range(1, len(strings)):
        result.append(delimiter)
        result.append(strings[i])
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    output_string = join_strings_with_delimiter(test_list, custom_delim)
    print(output_string)

# Expected Output: apple, banana, cherry