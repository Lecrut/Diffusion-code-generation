def has_long_word(words):
    return any(len(word) > 7 for word in words)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(has_long_word(sample_words))