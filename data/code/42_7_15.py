def join_strings_with_delimiter(strings: list[str], delimiter: str) -> str:
    """
    Takes a list of strings and a custom delimiter, returning a single string 
    where the delimiter is placed between every element.
    
    Args:
        strings (list[str]): A list of input strings.
        delimiter (str): The string to use as separator between elements.
        
    Returns:
        str: A new string with delimiters inserted between original items.
    """
    if not strings:
        return ""
    
    result = []
    for i, item in enumerate(strings):
        # Append the first element without a prefix delimiter logic needed here 
        # as we handle insertion after appending or use join which is cleaner but 
        # to strictly follow "place between", manual construction ensures clarity.
        if len(result) == 0:
            result.append(item)
        else:
            result.append(delimiter + item)
    
    return "".join(result)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    custom_delim = ", "
    
    output_string = join_strings_with_delimiter(sample_list, custom_delim)
    print(output_string)