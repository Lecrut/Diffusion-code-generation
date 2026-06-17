import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'\b\w+\b', f' {text} ')) and len(match.group()) > 0]
if __name__ == '__main__':
    sample = "Hello, world! This is a test string. Python3."
    result = split_words(sample)
    print(result)