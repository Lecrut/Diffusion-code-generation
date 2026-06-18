import re
def split_words(text: str) -> list[str]:
    pattern = r'\b\w+\b'
    return re.findall(pattern, text)
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. How are you?"
    result = split_words(sample_text)
    print(result)