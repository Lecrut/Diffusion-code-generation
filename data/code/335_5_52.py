import sys
def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    return words
if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result = split_sentence(sample_input)
    print(result)