import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not isinstance(delimiter, str):
        raise TypeError(f"Delimiter must be a string, got {type(delimiter).__name__}")

    return delimiter.join(parts)

def main() -> None:
    # Hard-coded sample values to ensure no user input or file access is required.
    sample_parts = ["apple", "banana", "cherry"]
    
    try:
        result_string = join_string_parts(sample_parts, default_delimiter=",")
        print(result_string)
    except TypeError as e:
        # Handle invalid input types gracefully without printing extra debug info beyond the error.
        sys.stderr.write(f"Error: {e}\n")

if __name__ == '__main__':
    main()