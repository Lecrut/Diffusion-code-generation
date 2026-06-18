import sys

def join_parts(parts_list: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not all(isinstance(part, str) for part in parts_list):
        raise TypeError("All input elements must be strings.")
    
    return delimiter.join(parts_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    sample_parts = ["apples", "bananas", "cherries"]
    sample_delimiter = "|"
    
    try:
        result_str = join_parts(sample_parts, sample_delimiter)
        print(result_str)
    except TypeError as e:
        # Handle invalid input types gracefully while keeping it non-interactive.
        sys.stderr.write(f"Error: {e}\n")