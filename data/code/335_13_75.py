def split_sentence(sentence: str) -> list[str]:
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello World This is an efficient function"
    result_words = split_sentence(sample_sentence)
    print("Input Sentence:", repr(sample_sentence))
    print("Split Words: ", result_words)