def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    result = split_words(sample_text)
    print(result)