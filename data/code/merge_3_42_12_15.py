import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of strings with the specified delimiter."""
    if not all(isinstance(part, (str, bytes)) and isinstance(delimiter, (str, bytes)) for part in parts):
        raise TypeError("All input parts must be string-like objects.")

    result_parts = [part.decode() if isinstance(part, bytes) else part for part in parts]
    return delimiter.join(result_parts)

if __name__ == "__main__":
    sample_values = ["apple", "banana", "cherry"]
    
    try:
        combined_string = join_string_parts(sample_values)
        print(combined_string, end="")
    except (TypeError, ValueError):
        sys.stderr.write("Error: Invalid input types detected.\n")