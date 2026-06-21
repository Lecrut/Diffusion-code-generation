def word_exists(word):
    predefined_words = {'apple', 'banana', 'cherry'}
    return word in predefined_words
if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))