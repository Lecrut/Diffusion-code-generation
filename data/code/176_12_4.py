def find_alphabetic_words(sentence):
    return [word for word in sentence.split() if word.isalpha()]

if __name__ == '__main__':
    sample_sentence = "Hello, World! 123 Python is fun."
    print(find_alphabetic_words(sample_sentence))