def split_sentence(sentence: str) -> list[str]:
    return sentence.strip().split()
if __name__ == '__main__':
    sample_sentence = "  Hello World! This is a test string.  "
    result_words = split_sentence(sample_sentence)
    print(f"Input: '{sample_sentence}'")
    print(f"Output words: {result_words}")