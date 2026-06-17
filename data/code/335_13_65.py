def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is an example of efficient Python code."
    result_words = split_sentence(sample_sentence)
    print(f"Input: {sample_sentence}")
    print(f"Words: {result_words}")