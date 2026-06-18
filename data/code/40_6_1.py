import re

def get_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from the input text."""
    words = re.findall(r'\b\w+\b', text.lower())
    return [word[0] for word in words if len(word) > 1]

if __name__ == '__main__':
    sample_input = """Hello world, this is a test.
Multiple lines here to show handling of newlines correctly."""

    print(get_first_letters(sample_input))