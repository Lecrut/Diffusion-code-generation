def is_word_long(word):
    minimum_length = 8
    return len(word) > minimum_length

if __name__ == '__main__':
    test_words = ["apple", "pineapple", "kiwi", "watermelon"]
    for word in test_words:
        print(f"The word '{word}' meets the criteria: {is_word_long(word)}")