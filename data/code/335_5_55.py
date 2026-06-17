import sys
def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    return words
if __name__ == '__main__':
    sample_input = "Hello world this is a test command line utility"
    result_words = split_sentence(sample_input)
    for word in result_words:
        print(word)
    sys.exit(0)