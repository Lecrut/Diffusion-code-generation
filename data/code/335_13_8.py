def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, this is an example of Pythonic code execution."
    result_words = split_sentence(sample_sentence)
    print(f"Input: {sample_sentence}")
    print(f"Output words: {result_words}")