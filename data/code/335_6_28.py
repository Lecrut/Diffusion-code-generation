import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'\b([a-zA-Z]+)\b', f' {text} ')) and match.group(1)] or []
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Python 3.9."
    result = split_words(sample)
    print(result)