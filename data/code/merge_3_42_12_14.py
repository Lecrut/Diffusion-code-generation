import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        delimiter (str): The separator between each part, defaults to comma.
        
    Returns:
        str: The resulting concatenated string.
        
    Raises:
        TypeError: If any element in 'parts' is not a string or if 'delimiter' 
                  is not a string.
    """
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements must be strings, got {type(item).__name__}")
    
    if not isinstance(delimiter, str):
        raise TypeError("Delimiter must be a string")

    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_parts = ["apple", "banana", "cherry"]
    
    try:
        result_string = join_string_parts(sample_parts, ",")
        print(result_string)
    except TypeError as e:
        # Error handling for invalid input types is included in the function logic above.
        sys.stderr.write(f"Error: {e}\n")