def get_words(sentence):
    words = sentence.split()
    return [word.lower() for word in words]

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test."
    print(get_words(sample_sentence))