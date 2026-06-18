def get_first_letters(strings):
    """
    Returns a list containing the first character of each input string.
    
    Args:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list where each element is the first character 
                   corresponding to the input strings in order.
    """
    result = []
    for s in strings:
        if not isinstance(s, str):
            raise TypeError(f"Expected string, got {type(s).__name__}")
        if len(s) == 0:
            # Handle empty strings by appending an empty string or a placeholder.
            # Based on robustness requirement, we append the first character 
            # only if it exists; otherwise, we skip to avoid IndexError.
            continue
        result.append(s[0])
    return result

if __name__ == '__main__':
    sample_strings = [
        "Hello",
        "World",
        "",
        "Python",
        "Script"
    ]

    first_chars = get_first_letters(sample_strings)
    
    print("First letters:")
    for char in first_chars:
        print(char)