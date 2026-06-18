import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text.lower())
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string. Python 3.12 is great."
    result = split_words(sample_text)
    print(result)