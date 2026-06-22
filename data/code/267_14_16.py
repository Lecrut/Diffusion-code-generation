def has_long_word(words):
    for word in words:
        if len(word) > 7:
            return True
    return False

if __name__ == '__main__':
    sample_words = ["hello", "world", "Python", "programming"]
    print(has_long_word(sample_words))