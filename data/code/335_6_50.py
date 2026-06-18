import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b[\w]+', text)
if __name__ == '__main__':
    sample = "Hello, world! This is a test string."
    result = split_words(sample)
    print(result)