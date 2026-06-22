def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "Learning Python is exciting and rewarding"
    result = extract_words(test_sentence)
    print(result)