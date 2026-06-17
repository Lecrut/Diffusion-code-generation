import sys
def split_words(text: str) -> list[str]:
    words = text.split()
    return words
if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    result = split_words(sample_text)
    print(result)