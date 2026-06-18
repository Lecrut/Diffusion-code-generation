def concatenate_strings(strings: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.
    
    Args:
        strings (list[str]): A list of input strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".
        
    Returns:
        str: The resulting concatenated string.
    """
    return delimiter.join(strings)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    input_list = ["Hello", "World", "Python"]
    chosen_delimiter = ", "

    result_string = concatenate_strings(input_list, chosen_delimiter)
    
    print(result_string)