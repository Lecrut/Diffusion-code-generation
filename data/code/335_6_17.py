import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'[a-zA-Z]+', f' {text} ')) and not match.group(0).strip().isdigit()] or []
if __name__ == '__main__':
    sample = "Hello, world! This is a test. 123 numbers here."
    result = split_words(sample)
    print(result)