def get_first_letters(string_list):
    """
    Returns a new list containing only the first character of each string 
    in the input list using list comprehension for efficiency.
    
    Args:
        string_list (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string.
                  If an empty string exists, it will be omitted from the result based on slicing behavior 
                  which returns an empty slice for "". To ensure a single char per non-empty item or skip empty items?
                  Given typical constraints: we assume strings are non-empty. 
                  However, if a string is empty, s[0] raises IndexError. 
                  The task says "first character of each string", implying existence. 
                  We'll proceed assuming valid input (non-empty strings) to avoid runtime errors on edge cases not specified.
    """
    return [s[0] for s in string_list if len(s) > 0]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    result = get_first_letters(sample_strings)
    print(result)