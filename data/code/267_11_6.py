def filter_long_words(words):
    long_words = [word for word in words if len(word) > 4]
    return long_words

if __name__ == '__main__':
    sample_words = ["apple", "bee", "cat", "dog", "elephant", "frog"]
    filtered_words = filter_long_words(sample_words)
    print(filtered_words)