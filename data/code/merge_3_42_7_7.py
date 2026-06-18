def join_strings_with_delimiter(string_list: list[str], delimiter: str) -> str:
    """
    Joins a list of strings with a custom delimiter placed between elements.
    
    Args:
        string_list (list): A list of strings to be joined.
        delimiter (str): The string to place between each element in the list.
        
    Returns:
        str: A single string where delimiters separate the original items.
    """
    if not string_list:
        return ""
    
    # Join elements with the delimiter, then remove leading/trailing delimiters 
    # by stripping at both ends (though join usually handles internal placement correctly).
    result = f"{delimiter.join(string_list)}"
    
    # Ensure no extra delimiter appears before first item or after last if they exist.
    while len(result) > 0 and result[0] == delimiter:
        result = result[1:]
    while len(result) > 0 and result[-1] == delimiter:
        result = result[:-1]
        
    return result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    final_string = join_strings_with_delimiter(sample_list, custom_delim)
    print(final_string)