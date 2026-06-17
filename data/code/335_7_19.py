def extract_words(sentence: str) -> list:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world this is a test of pure python function"
    result = extract_words(sample_sentence)
    print(result)