def join_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter, returning a single string 
    where the delimiter is placed between every element.
    
    Args:
        strings (list[str]): List of input strings to be joined.
        delimiter (str): The string used as a separator between elements.
        
    Returns:
        str: A new string with elements separated by the custom delimiter.
    """
    if not strings:
        return ""
    
    result = [strings[0]]
    for i in range(1, len(strings)):
        result.append(delimiter + strings[i])
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_list = ["apple", "banana", "cherry"]
    custom_sep = ", : "
    
    output_string = join_with_delimiter(test_list, custom_sep)
    print(output_string)  # Expected Output: apple, : banana, : cherry