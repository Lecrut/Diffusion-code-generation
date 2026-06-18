def concatenate_strings(first_string: str, second_string: str) -> str:
    """
    Appends the second string to the first using an f-string for clarity.
    
    Args:
        first_string (str): The initial string component.
        second_string (str): The string to be appended.
        
    Returns:
        str: A new concatenated string formed by appending the second 
             argument to the first argument of this function.
    """
    return f"{first_string}{second_string}"

if __name__ == '__main__':
    sample_first = "Hello"
    sample_second = "World"
    
    result = concatenate_strings(sample_first, sample_second)
    print(result)