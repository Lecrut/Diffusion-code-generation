class WordFilter:
    MIN_LENGTH = 4

    @staticmethod
    def is_word_long(word: str) -> bool:
        return len(word) > WordFilter.MIN_LENGTH

if __name__ == '__main__':
    words = ["short", "longerword", "test"]
    long_words = [word for word in words if WordFilter.is_word_long(word)]
    print(long_words)