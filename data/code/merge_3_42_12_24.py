import sys

def join_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not all(isinstance(part, str) for part in parts):
        raise TypeError("All input elements must be strings.")
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or external dependencies are needed.
    sample_parts = ["apple", "banana", "cherry"]

    try:
        result_string = join_parts(sample_parts, ",")
        print(result_string)
    except TypeError as e:
        error_message = f"Error: {e}"
        # In a production environment, this might be logged; here we just store it.
        _error_log = [error_message]