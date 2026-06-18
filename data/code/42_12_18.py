import sys

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """Join a sequence of string parts with the specified delimiter."""
    if not isinstance(delimiter, str):
        raise TypeError("Delimiter must be a string.")
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_parts = ["apple", "banana", "cherry"]
    result = join_string_parts(sample_parts, ",")
    print(result)