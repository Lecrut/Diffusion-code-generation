def split_words(text):
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello, World! This is a test of Pythonic string splitting."
    words = split_words(sample_text)
    print("Split result:", words)
    assert len(words) > 0 and isinstance(words[0], str), "Error: Split failed or returned non-string"