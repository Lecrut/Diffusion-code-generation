def is_word_long(word):
    MIN_LENGTH = 15
    return len(word) > MIN_LENGTH

if __name__ == '__main__':
    test_words = ["short", "thisisalongwordexample", "a_very_long_string_here_is_extremely_long"]
    results = {word: is_word_long(word) for word in test_words}
    print(results)