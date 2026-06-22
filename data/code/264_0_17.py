def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "Exploring the depths of Python programming is both challenging and rewarding!"
    result = extract_words(test_sentence)
    print(result)