predefined_words = {'apple', 'banana', 'cherry'}

def word_exists(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string.")
    return word.lower() in predefined_words

if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))