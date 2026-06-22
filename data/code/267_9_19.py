def is_word_long(word):
    return len(word) > 5

if __name__ == '__main__':
    sample_words = ["hello", "world", "Python", "programming"]
    for word in sample_words:
        print(f"The word '{word}' is long: {is_word_long(word)}")