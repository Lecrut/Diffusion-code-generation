import re
def split_words(text: str) -> list[str]:
    return [word for word in re.findall(r'\b\w+\b', text)]
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string. Python 3.12."
    result = split_words(sample_text)
    print(result)