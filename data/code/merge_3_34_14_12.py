"""Capitalize the first letter of each word in a string."""

def capitalize_words(text: str) -> str:
    """Return a copy of text with the first character of every word capitalized."""
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_input = "hello world from python"
    result = capitalize_words(sample_input)
    print(result)