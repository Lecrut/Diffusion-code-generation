def concatenate_strings(string_list: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.
    
    Args:
        string_list (list): A list of strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".
        
    Returns:
        str: A new string with all elements from the input list joined by the delimiter.
    """
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise TypeError("Input must be a list of strings.")
    
    return delimiter.join(string_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_data = ["Hello", "World", "Python"]
    custom_delimiter = "|"

    result_string = concatenate_strings(sample_data, custom_delimiter)
    
    print(f"Concatenated Result: '{result_string}'")