def get_first_letters(string_list):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Args:
        string_list (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding 
                   input string, or an empty string if the input string was empty.
    """
    return [s[0] if s else '' for s in string_list]

if __name__ == '__main__':
    sample_data = ["hello", "world", "", "python"]
    result = get_first_letters(sample_data)
    print(result)  # Output: ['h', 'w', '', 'p']