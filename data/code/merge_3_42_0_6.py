def concatenate_strings(strings: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.
    
    Args:
        strings (list): A list of strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".
        
    Returns:
        str: The resulting concatenated string.
    """
    if not isinstance(strings, list):
        raise TypeError("The first argument must be a list.")
    
    return delimiter.join(str(item) for item in strings)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed).
    sample_list = ["Hello", "World", "This", "is", "a", "test"]
    custom_delimiter = "|"

    result_string = concatenate_strings(sample_list, delimiter=custom_delimiter)
    
    print(f"Concatenated Result: {result_string}")