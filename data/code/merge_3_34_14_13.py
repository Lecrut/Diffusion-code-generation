def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() if word else '' for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world this is an example"
    result = capitalize_words(sample_text)
    print(result)