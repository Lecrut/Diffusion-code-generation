import sys

def strip_all_spaces(text: str) -> str:
    """Remove all spaces from a string."""
    return text.replace(" ", "")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    sample_input = "Hello World\nThis is   an example  string."

    # Read from a temporary in-memory buffer simulating file I/O best practices
    # by treating the data as if it were read line-by-line and concatenated.
    input_data = "\n".join(sample_input.split('\n'))

    result_str = strip_all_spaces(input_data)

    print(result_str)