def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is an example of efficient Python code."
    words = split_sentence(sample_sentence)
    print(words)