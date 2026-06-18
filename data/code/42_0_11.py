def concatenate_strings(strings: list[str], delimiter: str = ", ") -> str:
    """
    Concatenates a list of strings into a single string separated by a specified delimiter.

    Args:
        strings (list[str]): A list of input strings to be concatenated.
        delimiter (str): The separator string used between each element in the list. Defaults to ", ".

    Returns:
        str: The newly constructed concatenated string.

    Raises:
        TypeError: If 'strings' is not a list or if elements are not all strings.
    """
    if not isinstance(strings, list):
        raise TypeError(f"Expected list of strings, got {type(strings).__name__}")
    
    for item in strings:
        if not isinstance(item, str):
            raise TypeError("All elements in the input list must be strings.")

    return delimiter.join(map(str, strings))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external dependencies or user interaction is required.
    sample_data = ["Hello", "World", "Python"]
    
    # Define a custom delimiter for the demonstration (defaulting to ", ") if not specified otherwise here, 
    # though we will use the default behavior of join with an optional argument passed directly.
    result_default_delimiter = concatenate_strings(sample_data)
    
    result_custom_delimiter = concatenate_strings(
        sample_data, 
        delimiter=" | "  # Using a pipe separator for variety in this example
    )

    print("Concatenated with default delimiter:", repr(result_default_delimiter))