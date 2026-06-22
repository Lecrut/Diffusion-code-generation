def has_long_word(sentence):
    return any(len(word) > 6 for word in sentence.split())

if __name__ == '__main__':
    print(has_long_word("This is a test"))
    print(has_long_word("Hello world from Python"))