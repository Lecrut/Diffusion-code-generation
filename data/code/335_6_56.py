import re
def split_words(text: str) -> list[str]:
    return [word.strip(".,!?;:\"'") for word in re.findall(r"\b\w+\b", text)]
if __name__ == '__main__':
    sample = "Hello, world! This is a test. Can you handle punctuation?"
    result = split_words(sample)
    print(result)