def is_word_long(word):
    return len(word) > 5
if __name__ == '__main__':
    print(is_word_long('hello'))
    print(is_word_long('world'))
    print(is_word_long('Python'))
    print(is_word_long(''))