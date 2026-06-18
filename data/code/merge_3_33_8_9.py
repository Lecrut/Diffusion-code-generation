def remove_internal_spaces(strings):
    """
    Returns a new list where every string in the input has its internal spaces removed.
    
    Args:
        strings (list of str): The list of strings to process.
        
    Returns:
        list of str: A new list with internal whitespace stripped from each element.
    """
    return [s.strip() for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_list = ["hello world", "  python   code ", "single word"]
    
    result = remove_internal_spaces(sample_list)
    
    print("Input:", sample_list)
    print("Output:", result)