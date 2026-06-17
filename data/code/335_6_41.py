import re
def split_words(text: str) -> list[str]:
    return [word for word in re.findall(r'\b\w+\b', text)]
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Python 3."
    result = split_words(sample_text)
    print(result)