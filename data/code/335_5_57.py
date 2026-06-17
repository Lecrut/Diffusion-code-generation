import sys
def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello World This is a test"
    result_words = split_sentence(sample_input)
    print(" ".join(result_words))
    sys.exit(0)