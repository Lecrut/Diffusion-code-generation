import sys

def join_parts(parts: list[str], delimiter: str) -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not all(isinstance(p, str) for p in parts):
        raise TypeError("All input parts must be strings.")
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of no user input.
    sequence = ["apple", "banana", "cherry"]
    
    try:
        result_string = join_parts(sequence, ",")
        print(result_string)
    except (IndexError, TypeError) as e:
        error_message = f"Invalid input provided: {e}"
        sys.stderr.write(f"{error_message}\n")