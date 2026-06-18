import sys

def remove_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return "".join(char for char in text if not (char == " "))

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user input.
    # Simulates reading a multi-line string from standard input via file I/O best practices.
    sample_input = """Hello World
This is   another line with spaces."""

    # Best practice: Read the entire buffer at once for simplicity in this context, 
    # though for very large files one might iterate or use generators to save memory.
    # Here we simulate reading from stdin by assigning our sample input directly 
    # into a variable that would represent sys.stdin.read() if actual I/O were used.

    result = remove_all_spaces(sample_input)

    print(result)