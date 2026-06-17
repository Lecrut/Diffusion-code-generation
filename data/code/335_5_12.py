import sys
def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = split_sentence(sample_input)
    print(" ".join(result))
    sys.exit(0)