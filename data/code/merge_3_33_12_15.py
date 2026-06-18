import sys

def strip_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return "".join(char for char in text if not (char == ' ') or ord(char) > 32 and char != '\t' and char != '\n')

if __name__ == '__main__':
    sample_input = "Hello world\nThis is a test.\n   Multiple   spaces here."

    # Simulate reading from standard input using the hard-coded value directly.
    raw_data = sample_input
    
    result = strip_all_spaces(raw_data)
    
    print(result)