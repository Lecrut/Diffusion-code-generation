def capitalize_words(text: str) -> str:
    """Capitalize only the first letter of each word in a string."""
    return ' '.join(word.capitalize() if word else '' for word in text.split())

if __name__ == '__main__':
    sample_string = "hello world from python module"
    result = capitalize_words(sample_string)
    print(result)  # Output: Hello World From Python Module