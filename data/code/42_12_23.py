import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Join a sequence of string parts with a specified delimiter.

    Args:
        parts (list): A list of strings to be joined.
        delimiter (str): The separator between the strings, defaults to ','.

    Returns:
        str: The resulting concatenated string separated by the delimiter.
    
    Raises:
        TypeError: If 'parts' is not a list or contains non-string elements.
    """
    if not isinstance(parts, list):
        raise TypeError(f"Expected a list of strings, got {type(parts).__name__}")

    for i, part in enumerate(parts):
        if not isinstance(part, str):
            raise TypeError(
                f"All parts must be strings. Part at index {i} is of type "
                f"{type(part).__name__}"
            )

    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, or network access.
    sample_parts = ["apple", "banana", "cherry"]
    
    try:
        result = join_string_parts(sample_parts)
        print(result)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)