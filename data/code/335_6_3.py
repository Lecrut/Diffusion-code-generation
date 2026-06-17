import re
def split_words(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text.lower())
if __name__ == '__main__':
    sample = "Hello, world! This is a test string with numbers 123 and symbols @#$."
    result = split_words(sample)
    print(result)