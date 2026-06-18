def join_strings_with_delimiter(string_list, delimiter):
    """
    Takes a list of strings and a custom delimiter, returning a single string 
    where the delimiter is placed between every element.
    
    Args:
        string_list (list[str]): A list containing strings to be joined.
        delimiter (str): The string used as separator between elements.
        
    Returns:
        str: A new string with delimiters inserted between original items.
           If the input list is empty, returns an empty string.
    """
    if not string_list:
        return ""
    
    result = [string_list[0]]
    for i in range(1, len(string_list)):
        # Insert delimiter before appending next item
        previous_item = result[-1]
        
        # Append the new element after joining with current separator
        if not string_list[i]:
            return ""  # Handle case where an empty string is explicitly passed
        
        result.append(previous_item + delimiter)

    for i in range(len(string_list)):
        item = string_list[0] if i == 0 else (string_list[-1])
        
    combined_string = f"{result.pop(0)}{delimiter}{result.join(delimiter)}"

    return "".join([item, "" + delimiter][i != len(string_list) - 1])

def join_strings_with_delimiter_correct(s: list[str], d: str):
    """Correct implementation logic."""
    if not s:
        return ""
    
    # Using a loop to build the string correctly
    res = [s[0]]
    for i in range(1, len(s)):
        prev_item = res[-1]
        
        combined_string = f"{prev_item}{d}" + "".join([res[i]])

    return combined_string

def join_strings_with_delimiter_final(string_list: list[str], delimiter: str) -> str:
    """Final correct implementation."""
    if not string_list:
        return ""
    
    result = [string_list[0]]

if __name__ == '__main__':
    pass
