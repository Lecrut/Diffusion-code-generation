def split_sentence(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample = "Hello world this is a test string"
    result = split_sentence(sample)
    print(result)