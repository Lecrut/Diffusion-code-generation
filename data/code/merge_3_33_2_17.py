import re

def remove_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return re.sub(r"\s+", "", text)

if __name__ == '__main__':
    # Hard-coded sample multi-line strings to test without user interaction.
    samples = [
        "Hello world, this is a test.",
        "  Multiple   spaces     here? ",
        "No extra spacing needed.",
    ]

    for text in samples:
        result = remove_all_spaces(text)
        print(result)