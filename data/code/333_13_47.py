import string
def extract_first_letters(text: str) -> list[str]:
    return [word[0] for word in text.split() if len(word) > 1 and not any(c.isupper() for c in word)]
if __name__ == '__main__':
    sample = "hello world python programming"
    result = extract_first_letters(sample)