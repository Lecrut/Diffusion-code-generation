import sys
def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result_words = split_sentence(sample_input)
    print(result_words)
    sys.exit(0)