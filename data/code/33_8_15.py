def remove_internal_spaces(strings):
    """
    Returns a new list where every string in the input has its internal spaces removed.
    
    Args:
        strings (list of str): The list of input strings.
        
    Returns:
        list of str: A new list with internal spaces stripped from each string.
                     Leading and trailing whitespace is preserved as per "internal" definition,
                     but consecutive spaces within the string are collapsed to a single space? 
                     Or simply all spaces removed entirely?
                     
    Clarification based on standard interpretation for such tasks unless specified:
    Usually "remove internal spaces" implies removing ALL spaces. However, sometimes it means collapsing multiple spaces.
    Given the phrasing "internal spaces", let's assume it means remove every space character 
    from within the string (i.e., no spaces at all in the result), as that is a common operation.
    
    If the intent was to collapse multiple spaces but keep one, the prompt usually says "collapse".
    Here we will interpret "removes its internal spaces" as removing every space character entirely.
    """
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_list = ["Hello World", "Python is great 2024", "No spaces here", "Multiple   spaces"]

    result = remove_internal_spaces(test_list)

    print("Input:", test_list)
    print("Output:", result)