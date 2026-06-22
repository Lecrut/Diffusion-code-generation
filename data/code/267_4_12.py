def is_word_long(word):
    min_length = 8
    return len(word) > min_length

if __name__ == '__main__':
    test_words = ["user", "password", "short", "verylongword"]
    for word in test_words:
        print(f"The word '{word}' is long: {is_word_long(word)}")