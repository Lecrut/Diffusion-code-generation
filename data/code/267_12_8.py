def has_long_word(sentence):
    if not isinstance(sentence, str):
        raise ValueError('Input must be a string')
    return any((len(word) > 6 for word in sentence.split()))
if __name__ == '__main__':
    print(has_long_word('hello world'))
    print(has_long_word('programming is fun'))
    print(has_long_word(''))
    try:
        print(has_long_word(12345))
    except ValueError as e:
        print(e)