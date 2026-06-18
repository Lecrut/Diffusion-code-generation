import sys
def split_words(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    result = split_words(sample_sentence)
    print(" ".join(result))
    sys.exit(0)