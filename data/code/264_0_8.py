def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "Exploring new technologies is exciting and challenging"
    result = extract_words(test_sentence)
    print(result)