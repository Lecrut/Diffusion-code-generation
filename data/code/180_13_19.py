PREDEFINED_WORDS = {'apple', 'banana', 'cherry'}

def is_word_valid(word):
    if not isinstance(word, str) or not word.isalpha():
        raise ValueError("Word must be a non-empty alphabetic string")
    return True

def word_exists_in_set(word):
    is_word_valid(word)
    return word in PREDEFINED_WORDS

if __name__ == '__main__':
    print(word_exists_in_set('banana'))
    print(word_exists_in_set('grape'))