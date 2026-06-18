import re

def remove_spaces_from_strings(string_list):
    """
    Removes all internal spaces from every string in the provided list.
    
    Args:
        string_list (list of str): A list containing strings that may contain spaces.
        
    Returns:
        list of str: A new list where each original string has had its spaces removed.
                     Strings without spaces are returned unchanged.
                     
    Example:
        >>> remove_spaces_from_strings(["hello world", "no space here", "  multiple   spaces  ", "single"])
        ['helloworld', 'nospacehere', 'multiplespaces', 'single']
    """
    return [s.replace(' ', '') for s in string_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    sample_data = ["hello world", "programming is fun", "  leading and trailing spaces  ", "python"]
    
    result = remove_spaces_from_strings(sample_data)
    
    print("Original list:", sample_data)
    print("Processed list:", result)