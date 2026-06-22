def is_word_long(word):
    return len(word) > 10
if __name__ == '__main__':
    print(is_word_long('hello'))
    print(is_word_long('programming'))