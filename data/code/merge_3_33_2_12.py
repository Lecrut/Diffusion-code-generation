import sys

def remove_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return text.replace(" ", "")

if __name__ == '__main__':
    sample_input = "Hello World\nThis is a test.\n  Multiple   Lines."
    
    # Write to stdout directly using sys.stdout.write for efficiency and control,
    # avoiding interactive prompts or argument parsing.
    result = remove_all_spaces(sample_input)
    print(result)