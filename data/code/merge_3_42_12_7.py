def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list): A list containing strings to be joined.
        delimiter (str): The separator between items, defaults to comma.
        
    Returns:
        str: The resulting concatenated string.
        
    Raises:
        TypeError: If 'parts' is not a list or if any element in the list is not a string.
    """
    if not isinstance(parts, list):
        raise TypeError(f"Expected input to be a list, got {type(parts).__name__}")

    for idx, part in enumerate(parts):
        if not isinstance(part, str):
            raise TypeError(
                f"All elements must be strings. "
                f"Element at index {idx} is of type {type(part).__name__}"
            )
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files
    sample_parts = ["apple", "banana", "cherry"]
    result = join_string_parts(sample_parts, ",")
    print(result)

    # Additional test case with different delimiter and validation failure scenario (commented out for clean run)
    # invalid_input = [123]  # This would raise TypeError if uncommented in a real execution context