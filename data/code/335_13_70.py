def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split()
if __name__ == '__main__':
    sample_sentence = "  Hello, World! This is a test case for splitting sentences efficiently."
    result_words = split_sentence(sample_sentence)
    print("Input:", repr(sample_sentence))
    print("Output Words:")
    for word in result_words:
        print(repr(word))