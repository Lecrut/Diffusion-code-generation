def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, this is a Python script."
    result_words = split_sentence(sample_sentence)
    print(result_words)