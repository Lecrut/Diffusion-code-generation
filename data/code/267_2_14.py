def is_word_long(word):
    if not isinstance(word, str) or len(word.strip()) == 0:
        return False
    return len(word) > 5
if __name__ == '__main__':
    print(is_word_long('example'))
    print(is_word_long(''))
    print(is_word_long(123))
    print(is_word_long('a'))