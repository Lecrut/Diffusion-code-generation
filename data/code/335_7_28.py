def extract_words(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world this is a test"
    result = extract_words(sample)
    print(result)