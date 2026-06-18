def join_with_delimiter(items: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        items (list[str]): A list of string elements to be joined.
        delimiter (str): The string to place between each element.
        
    Returns:
        str: A single string where the delimiter is between every element.
             If the input list is empty, returns an empty string.
    
    Example:
        >>> join_with_delimiter(['a', 'b'], '-')
        "a-b"
        >>> join_with_delimiter([], ',')
        ""
    """
    if not items:
        return ""
    
    joined = [items[0]]
    for i in range(1, len(items)):
        joined.append(delimiter)
        joined.append(items[i])
    
    return "".join(joined)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    result = join_with_delimiter(sample_list, custom_delim)
    print(result)