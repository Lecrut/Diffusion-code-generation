MAX_WORD_LENGTH = 6

def has_long_word(sentence):
    words = sentence.split()
    return any((len(word) > MAX_WORD_LENGTH for word in words))
if __name__ == '__main__':
    print(has_long_word('hello world'))
    print(has_long_word('hello programming'))
    print(has_long_word('hi there'))
    print(has_long_word('testing is fun'))
    print(has_long_word('short words only'))