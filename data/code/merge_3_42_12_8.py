import sys

def join_parts(parts: list[str], delimiter: str = ",") -> str | None:
    """
    Joins a sequence of string parts with a specified delimiter.
    
    Args:
        parts (list): A list of strings to be joined.
        delimiter (str): The separator between the parts, defaults to ','.
        
    Returns:
        str: The resulting joined string if input is valid and not empty, 
             None otherwise.

    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    """
    # Validate that parts is exactly a list of strings
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"Expected string element but got {type(item).__name__}")

    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    # Simulating a sequence of parts that might come from an external source.
    sample_parts = ["apple", "banana", "cherry"]

    try:
        result_string = join_parts(sample_parts)
        print(result_string)
    except TypeError as e:
        print(f"Input error: {e}", file=sys.stderr)