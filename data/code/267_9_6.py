def is_word_long(word):
    return len(word) > 10
if __name__ == '__main__':
    test_words = ['short', 'thisisalongstring', 'onlyletters', 'this has a space', 'abcdefghij', 'a' * 11, '1234567890']
    for word in test_words:
        if not isinstance(word, str):
            raise ValueError(f'Input must be a string: {word}')
        result = is_word_long(word)
        print(f"Word: '{word}', Is Long: {result}")