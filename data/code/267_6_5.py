def is_long_word(word):
    threshold = 5
    return len(word) > threshold
if __name__ == '__main__':
    print(is_long_word('hello'))
    print(is_long_word('world'))