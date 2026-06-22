class WordFilter:
    MIN_LENGTH = 4

    @staticmethod
    def filter_long_words(words):
        return [word for word in words if len(word) > WordFilter.MIN_LENGTH]

if __name__ == '__main__':
    sample_words = ["apple", "bee", "cat", "dog", "elephant"]
    long_words = WordFilter.filter_long_words(sample_words)
    print(long_words)