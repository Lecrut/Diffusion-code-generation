def remove_spaces_from_strings(string_list):
    """
    Takes a list of strings as input and returns a new list where 
    internal spaces in each string have been removed. Strings with no 
    spaces remain unchanged, but leading/trailing whitespace is not trimmed; only 
    contiguous sequences between characters are eliminated if any exist within the bounds.
    
    Note: The requirement specifies "internal spaces". Standard interpretation for this type of task 
    often implies removing all space characters present in the string to avoid empty strings resulting from adjacent removals, 
    or specifically target single internal delimiters. Given the phrasing "every string... has its internal spaces removed",
    a robust approach is to remove every occurrence of the ' ' character within each string entirely, as this satisfies the condition for any space found inside (between indices).
    
    If the intent was only to collapse multiple single spaces into one while keeping leading/trailing intact or vice versa, 
    that would require more specific definition. Here we assume "remove internal spaces" means removing all ' ' characters from each string.

    Args:
        string_list (list of str): The input list containing strings.

    Returns:
        list of str: A new list with the same strings but without any space characters (' ').
    
    Example:
        >>> remove_spaces_from_strings(["hello world", "test"])
        ['helloworld', 'test']
    """
    result = []
    for s in string_list:
        # Remove all occurrences of space character from the string
        cleaned_s = ''.join(char if char != ' ' else '' for char in s)
        result.append(cleaned_s)
    
    return result

if __name__ == '__main__':
    sample_input = ["hello world", "goodbye  there", "no spaces here", "", "   leading and trailing "]
    output_list = remove_spaces_from_strings(sample_input)
    print("Input:", sample_input)
    print("Output:", output_list)