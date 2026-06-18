def concatenate_strings(input_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single new string, 
    separated by a specified delimiter.
    
    Args:
        input_list (list[str]): List of strings to be concatenated.
        delimiter (str): The separator string used between each element in the list.
        
    Returns:
        str: A single string with elements from the list joined by the delimiter.
    """
    return delimiter.join(input_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # or network access is required for execution.
    
    sample_strings = ["Hello", "world!", "Python"]
    chosen_delimiter = " | "

    result_string = concatenate_strings(sample_strings, chosen_delimiter)
    
    print(result_string)