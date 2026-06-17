import re
def split_words(text: str) -> list[str]:
    return [word for word in text.split() if not (len(word) > 1 and any(c.isalpha() != c.uppercase() for c in word))]
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Python3."
    result = re.findall(r"\b[a-zA-Z]+\b", sample.lower())
    print(result)