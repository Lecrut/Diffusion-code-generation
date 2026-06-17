def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split(' ')
if __name__ == '__main__':
    sample_sentence = "  Hello, world! This is a test case for efficiency."
    result_words = split_sentence(sample_sentence)
    print(result_words)