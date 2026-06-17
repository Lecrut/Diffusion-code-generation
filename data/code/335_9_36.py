import re
def split_words(text: str) -> list[str]:
    return [word for word in text.split()] if not re.search(r'\s', text) else re.findall(r'[\w]+', text)
if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    words = split_words(sample_text)
    print(words)