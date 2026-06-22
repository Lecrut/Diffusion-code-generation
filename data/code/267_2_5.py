def is_word_long(word):
    if not isinstance(word, str) or word == '':
        return False
    return len(word) > 5
if __name__ == '__main__':
    print(is_word_long('hello'))
    print(is_word_long('worldly'))
    print(is_word_long(''))
    print(is_word_long(123))