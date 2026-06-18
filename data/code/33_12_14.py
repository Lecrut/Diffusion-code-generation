import sys

def strip_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return "".join(char for char in text if not (char == " "))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user interaction, command-line arguments, or network access is used.
    multi_line_string = """Hello World from Python. 
This line has multiple spaces between words and at the end."""

    result = strip_all_spaces(multi_line_string)
    print(result)