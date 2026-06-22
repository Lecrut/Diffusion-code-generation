import string

def has_punctuation_or_symbols(text):
    if not isinstance(text, str):
        return False
    punct_set = set(string.punctuation)
    for char in text:
        if char in punct_set:
            return True
    return False

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "Hello, World!",
        "No symbols here",
        "Python 3.9 is cool.",
        "100%",
        "abc",
        "!@#$%",
        ""
    ]
    for text in sample_texts:
        result = has_punctuation_or_symbols(text)
        print(f"Text: '{text}' -> Contains punctuation/symbols: {result}")