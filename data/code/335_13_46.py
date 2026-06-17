def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world Python programming is fun"
    result_words = split_sentence(sample_sentence)
    print("Original:", repr(sample_sentence))
    print("Words:   ", result_words)