def join_strings_with_custom_delimiter(string_list: list, delimiter: str) -> str:
    """
    Joins a list of strings into a single string with a custom delimiter 
    placed between every element.
    
    Args:
        string_list (list): A list of strings to be joined.
        delimiter (str): The string to insert between elements.
        
    Returns:
        str: A single string with the delimiter inserted between items.
            
    Example:
        >>> join_strings_with_custom_delimiter(["a", "b", "c"], ",") 
        'a,b,c'
    """
    if not string_list:
        return ""
    
    result = [string_list[0]]
    for i in range(1, len(string_list)):
        # Join the current accumulator with the next item using the delimiter only once between them
        # We construct the new element as (previous_element + "delimiter" + current_item) 
        # But to keep it efficient and correct even with empty strings or special cases:
        result.append(delimiter.join([string_list[i]]) if len(result) > 1 else string_list[i])

    return delimiter.join(string_list)

if __name__ == '__main__':
    sample_data = ["Python", "is", "awesome"]
    custom_delim = "-"
    
    # Calculate the result using our function
    final_output = join_strings_with_custom_delimiter(sample_data, custom_delim)
    
    print(f"Joined: '{final_output}'")