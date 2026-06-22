def is_long_word(word):
    return len(word) > 5
if __name__ == '__main__':
    print(is_long_word('hello'))
    print(is_long_word('worldly'))