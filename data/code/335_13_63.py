def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, world! This is an example."
    words = split_sentence(sample_sentence)
    print("Split result:", words)