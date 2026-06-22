def extract_first_word(sentence):
    words = sentence.split()
    if words:
        return words[0]
    return ""

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    print(extract_first_word(sample_sentence))