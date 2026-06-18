import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'\b\w+\b', f' {text} ')) and match.group()]
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Python3."
    result = split_words(sample)
    print(result)