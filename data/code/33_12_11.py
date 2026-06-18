import re

def remove_all_spaces(text: str) -> str:
    """Removes all spaces from a given string using regular expressions."""
    return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    sample_string = "Hello world. This is a test.\n\n  Spaces everywhere   here."
    result = remove_all_spaces(sample_string)
    print(result)