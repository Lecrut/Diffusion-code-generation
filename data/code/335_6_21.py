import re
def split_words(text: str) -> list[str]:
    return [word for word in text.split() if not any(ord(c) > 126 and ord(c) < 33 for c in word)]
if __name__ == '__main__':
    sample = "Hello, world! This is a test... string."
    result = split_words(sample)
    print(result)