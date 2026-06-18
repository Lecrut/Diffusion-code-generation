import re

def remove_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return ''.join(char for char in text if not (char == ' ' or char == '\t' or char == '\n'))

if __name__ == '__main__':
    sample_multi_line = "Hello world\nThis is a test.\nThe end."

    # Process the hard-coded sample string to remove all spaces and whitespace characters.
    result = remove_spaces(sample_multi_line)

    print(result)