def word_exists(word):
    predefined_words = {'apple', 'banana', 'cherry'}
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return word in predefined_words

if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))