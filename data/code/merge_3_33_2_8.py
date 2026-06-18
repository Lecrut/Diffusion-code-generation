import sys

def remove_all_spaces(text: str) -> str:
    """Removes all spaces from the input string, both internal and external."""
    return "".join(text.split())

if __name__ == '__main__':
    sample_input = """Hello World! This is a test.   Spaces everywhere.  No quotes needed. Just clean text output."""

    # Using standard I/O best practices via sys.stdin for potential multi-line scenarios,
    # but since the requirement specifies no interactive input and hard-coded samples,
    # we capture the sample string directly to ensure it runs without user interaction or external files.
    raw_input = """Hello World! This is a test.   Spaces everywhere.  No quotes needed. Just clean text output."""

    processed_output = remove_all_spaces(raw_input)

    print(processed_output)