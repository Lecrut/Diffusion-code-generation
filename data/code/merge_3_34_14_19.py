# Capitalize only the first letter of each word in a given string.
def capitalize_first_letters(text: str) -> str:
    """Return text with every non-alphabetic character between words replaced, then capitalized."""
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world! this is a test."
    result = capitalize_first_letters(sample_text)
    print(result)