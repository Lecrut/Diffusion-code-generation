import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list): A list containing strings to be joined.
        delimiter (str): The separator between elements in the resulting string. Defaults to ','.

    Returns:
        str: The concatenated result of joining all parts using the provided delimiter.

    Raises:
        TypeError: If any element in 'parts' is not a string or if 'delimiter' is not a string.
    """
    for part in parts:
        if not isinstance(part, str):
            raise TypeError(f"Expected string type but got {type(part).__name__}")

    if not isinstance(delimiter, str):
        raise TypeError("Delimiter must be a string")

    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access.
    sample_parts = ["hello", "world", "this", "is", "a", "test"]