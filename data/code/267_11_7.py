def filter_long_words(words):
    return [word for word in words if len(word) > 4]

if __name__ == '__main__':
    sample_words = ["apple", "bee", "cat", "dog", "elephant"]
    print(filter_long_words(sample_words))