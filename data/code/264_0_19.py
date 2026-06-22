def extract_words(sentence):
    words = sentence.split()
    return words

if __name__ == '__main__':
    test_sentence = "This is an example of extracting words from a sentence."
    result = extract_words(test_sentence)
    print(result)