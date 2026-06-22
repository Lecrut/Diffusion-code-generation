LONG_WORD_THRESHOLD = 10

def is_word_long(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    test_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in test_words:
        print(is_word_long(word))