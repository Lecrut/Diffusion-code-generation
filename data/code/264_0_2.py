def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "Python programming is fun and educational"
    result = extract_words(test_sentence)
    print(result)