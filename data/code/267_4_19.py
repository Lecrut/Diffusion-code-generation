LONG_WORD_THRESHOLD = 10

def is_long_word(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    test_words = ["cat", "example", "apple", "banana", "cherry"]
    for word in test_words:
        print(f"The word '{word}' is long: {is_long_word(word)}")