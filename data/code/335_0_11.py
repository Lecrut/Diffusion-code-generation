import sys
def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello, world! This is Python."
    result = split_words(sample_text)
    print(result)
    sys.exit(0)