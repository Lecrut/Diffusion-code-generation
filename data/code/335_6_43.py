import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text.lower())
if __name__ == '__main__':
    sample = "Hello, world! How are you? I'm fine."
    result = split_words(sample)
    print(result)