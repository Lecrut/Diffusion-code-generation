def remove_internal_spaces(strings):
    """
    Returns a new list where every string in the input has its internal spaces removed.
    
    Args:
        strings (list of str): The list of strings to process.
        
    Returns:
        list of str: A new list with internal spaces stripped from each string.
    """
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    sample_data = ["hello world", "python is great 2024", "no_spaces_here"]
    result = remove_internal_spaces(sample_data)
    print(result)