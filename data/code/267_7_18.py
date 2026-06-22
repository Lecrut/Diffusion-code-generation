def is_long_word(word, min_length=10):
    if not isinstance(word, str) or len(word) <= min_length:
        return False
    return True

if __name__ == '__main__':
    print(is_long_word("short"))
    print(is_long_word("this is a long word"))