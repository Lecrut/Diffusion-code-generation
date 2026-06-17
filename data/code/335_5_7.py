import sys
def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    return words
if __name__ == '__main__':
    sample_input = "Hello world from Python"
    result_words = split_sentence(sample_input)
    print(" ".join(result_words))