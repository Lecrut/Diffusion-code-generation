def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split()
if __name__ == '__main__':
    sample_sentence = "  Hello, World! This is a test. Pythonic code."
    words = split_sentence(sample_sentence)
    print(words)