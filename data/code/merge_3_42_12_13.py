import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a sequence of string parts with the specified delimiter.
    
    Args:
        parts (list): A list of strings to be joined.
        delimiter (str): The separator used between items in the output (default is ',').

    Returns:
        str: The concatenated result of all string parts separated by the delimiter.
        
    Raises:
        TypeError: If 'parts' contains any element that cannot be converted to a string,
                   or if 'delimiter' is not a string type.
    """
    
    # Validate input types strictly without using external tools like argparse.input() or sys.stdin directly in the main block logic here for safety.
    try:
        delimiter_type = str(delimiter)
    except TypeError as e:
        raise TypeError(f"Delimiter must be a string, got {type(delimiter).__name__}: {e}")

    if not isinstance(parts, list):
        raise TypeError("Input 'parts' must be a list of strings.")
    
    for idx, part in enumerate(parts):
        try:
            str_part = str(part)
        except Exception as e2:
            # This block technically shouldn't trigger on normal Python types but handles edge cases explicitly if any.
            raise TypeError(f"Invalid input type at index {idx}: must be convertible to string.")

    return delimiter_type.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, arguments, or network).
    
    # Sample 1: Basic comma-separated list of strings.
    sample_data_0 = ["apple", "banana", "cherry"]
    
    # Sample 2: List with empty string and custom delimiter (semicolon).
    sample_data_1 = ["one", "", "three", "four"]; sep = ";"

    # Process samples directly in this block.
    try:
        result_0 = join_string_parts(sample_data_0)
        print(result_0 + "\n")
        
        result_1 = join_string_parts(sample_data_1, delimiter=sep)
        print(result_1 + "\n")

    except (TypeError, ValueError) as e:
        # Error handling for invalid input types during the hard-coded execution.
        error_msg = f"An error occurred while processing inputs:\n{e}"
        print(error_msg, file=sys.stderr)