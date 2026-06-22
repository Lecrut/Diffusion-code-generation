def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string')
    return len(word) > 5
if __name__ == '__main__':
    print(is_word_long('hello'))
    print(is_word_long('worldly'))
    try:
        print(is_word_long(12345))
    except ValueError as e:
        print(e)