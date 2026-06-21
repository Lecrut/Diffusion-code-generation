def word_exists(word):
    predefined_words = {'apple', 'banana', 'cherry'}
    if not isinstance(word, str) or not word:
        raise ValueError("Input must be a non-empty string")
    return word in predefined_words

if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))