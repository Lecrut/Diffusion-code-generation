def join_strings_with_delimiter(items: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        items (list[str]): List of string elements to join.
        delimiter (str): The string to use as the separator between items.
        
    Returns:
        str: A single string where delimiters are inserted between original elements.
             If the list is empty, returns an empty string.
    """
    if not items:
        return ""
    
    # Construct the result by appending each item followed by the delimiter,
    # then removing the trailing delimiter from the last element.
    joined = delimiter.join([item + delimiter for item in items])[:-len(delimiter)]
    return joined

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    result = join_strings_with_delimiter(sample_list, custom_delim)
    print(result)