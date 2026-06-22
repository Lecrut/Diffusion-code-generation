def is_any_word_longer_than_six(string):
    return any(len(word) > 6 for word in string.split())

if __name__ == '__main__':
    print(is_any_word_longer_than_six("Hello world from Python"))
    print(is_any_word_longer_than_six("Short words only"))