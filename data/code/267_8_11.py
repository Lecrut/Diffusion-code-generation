def is_word_long(word):
    min_length = 5
    return len(word) > min_length
if __name__ == '__main__':
    print(is_word_long('testing'))
    print(is_word_long('short'))
    print(is_word_long(''))
    print(is_word_long('a'))
    print(is_word_long('hello'))