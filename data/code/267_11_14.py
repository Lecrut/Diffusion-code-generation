def filter_long_words(words: list) -> list:
    def is_word_long(word: str) -> bool:
        return len(word) > 4

    return [word for word in words if is_word_long(word)]

if __name__ == '__main__':
    sample_words = ["apple", "bee", "cat", "dog", "elephant"]
    long_words = filter_long_words(sample_words)
    print(long_words)