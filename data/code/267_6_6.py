def is_word_long(word):
    return len(word) > 10

if __name__ == '__main__':
    test_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in test_words:
        print(is_word_long(word))