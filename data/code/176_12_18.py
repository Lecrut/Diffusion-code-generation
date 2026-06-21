def find_alphabetic_words(sentence):
    return [word for word in sentence.split() if word.isalpha()]

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    print(find_alphabetic_words(sample_sentence))