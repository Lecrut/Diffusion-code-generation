import re
def split_words(text: str) -> list[str]:
    return [word for word in text.split() if not any(ord(c) < 32 and c != ' ' for c in word)]
if __name__ == '__main__':
    sample = "Hello, world! This is a test string. Can you handle punctuation?"
    result = split_words(sample)
    print(result)