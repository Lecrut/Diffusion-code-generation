def is_long(word):
    if not isinstance(word, str) or len(word.strip()) == 0:
        return False
    return len(word) > 5
if __name__ == '__main__':
    print(is_long('hello'))
    print(is_long('world'))
    print(is_long(''))
    print(is_long(123))