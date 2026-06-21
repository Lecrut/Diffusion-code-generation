PREDEFINED_WORDS = {'apple', 'banana', 'cherry'}

def word_exists(word):
    return word in PREDEFINED_WORDS

if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))