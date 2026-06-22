def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "Splitting this sentence into words should be straightforward"
    result = extract_words(test_sentence)
    print(result)