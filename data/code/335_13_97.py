def split_sentence_into_words(sentence: str) -> list[str]:
    return sentence.rsplit()
if __name__ == '__main__':
    sample_sentence = "Hello, this is a Python script for testing efficiency."
    result_words = split_sentence_into_words(sample_sentence)
    print(" ".join(result_words))