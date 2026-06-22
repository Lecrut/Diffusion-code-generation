def check_word_length(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string')
    return len(word) > 5
if __name__ == '__main__':
    print(check_word_length('hello'))
    print(check_word_length('world'))