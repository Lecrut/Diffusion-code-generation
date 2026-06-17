import string
def split_words(text: str) -> list[str]:
    return [word for word in text.split() if not all(c == ' ' for c in word)]
if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with multiple   spaces."
    words = split_words(sample_text)
    print(words)