import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not all(isinstance(part, (str, bytes)) and isinstance(delimiter, (str, bytes)) for part in [parts] + [delimiter]):
        raise TypeError("All inputs must be strings or byte sequences.")
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    # Simulating reading from standard input by providing a list of string parts directly.
    sample_parts = ["apple", "banana", "cherry"]
    
    try:
        result_string = join_string_parts(sample_parts)
        print(result_string, end="")  # Print to stdout without newline if preferred, but default is fine too.
    except (TypeError, AttributeError) as e:
        sys.stderr.write(f"Error processing input: {e}\n")