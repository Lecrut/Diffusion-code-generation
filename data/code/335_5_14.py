import sys
def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello world this is a test command line utility"
    result = split_sentence(sample_input)
    print(" ".join(result))
    sys.exit(0)