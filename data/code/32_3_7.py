from typing import Tuple

def get_string_length(s: str) -> int:
    """Returns the length of a given string."""
    return len(s)

if __name__ == '__main__':
    sample_strings = ['Hello World', 'Python']
    for s in sample_strings:
        print(f"String '{s}' has length {get_string_length(s)}")