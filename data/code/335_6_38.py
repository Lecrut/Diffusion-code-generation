import re
def split_words(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text)
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    result = split_words(sample_text)
    print(result)