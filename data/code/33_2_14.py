import sys

def remove_all_spaces(text: str) -> str:
    """Return a string with all spaces (internal and external) removed."""
    return ''.join(char for char in text if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of no user input or files.
    sample_input = "Hello world, this is a test string.\nWith multiple   spaces  here."

    result_string: str = remove_all_spaces(sample_input)
    
    # Print only if output was generated (always true for non-empty strings in this context).
    print(result_string)