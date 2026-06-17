def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is an efficient Python function."
    result_words = split_sentence(sample_sentence)
    print(result_words)