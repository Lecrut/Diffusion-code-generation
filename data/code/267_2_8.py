def is_long_word(word):
    if not isinstance(word, str) or len(word.strip()) == 0:
        return False
    return len(word) > 5
if __name__ == '__main__':
    print(is_long_word('hello'))
    print(is_long_word('world'))
    print(is_long_word(''))
    print(is_long_word(123))