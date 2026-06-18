import sys

def join_parts(parts: list[str], delimiter: str = ",") -> str | None:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        delimiter (str): The separator between items in the output. Defaults to ','.

    Returns:
        str or None: The resulting joined string if input is valid and not empty, 
                     otherwise returns None to indicate an error condition for logging only.
    
    Raises:
        TypeError: If 'parts' contains non-string elements.
    """
    # Validate that all parts are strings
    for part in parts:
        if not isinstance(part, str):
            raise TypeError(f"All input parts must be strings, found {type(part).__name__}")

    if len(parts) == 0:
        return ""

    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies.
    raw_input_sequence = [
        "apple",
        "banana",
        "cherry"
    ]

    try:
        result_string = join_parts(raw_input_sequence)
        
        if result_string is None:
            # In a real application, we might log this error instead of printing.
            print("Error joined string is null.")
        else:
            print(result_string)
            
    except TypeError as e:
        # Handle invalid input types gracefully by printing the specific error message to stderr or stdout depending on design preference here.
        print(f"Input validation failed due to incorrect type: {e}", file=sys.stdout)