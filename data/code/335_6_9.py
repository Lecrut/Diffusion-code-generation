import re
def split_words(text: str) -> list[str]:
    return [word for word in text if (match := re.search(r'\b\w+\b', text)) and not match.group(0).startswith(' ') ]
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Python 3.12."
    result = split_words(sample)
    print(result)