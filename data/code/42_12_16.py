import sys

def join_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not all(isinstance(part, str) and part is not None for part in parts):
        raise TypeError("All input elements must be non-None strings.")
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    # Simulating a sequence of string parts from standard input.
    sample_parts = ["apple", "banana", "cherry"]

    try:
        result_string = join_parts(sample_parts)
        print(result_string)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)