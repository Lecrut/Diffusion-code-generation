class WordChecker:
    MIN_LENGTH = 10

    @staticmethod
    def is_long(word):
        return len(word) > WordChecker.MIN_LENGTH

if __name__ == '__main__':
    sample_words = ["short", "longerword", "thisisalongword", "medium", "verylongwordexample"]
    long_words = [word for word in sample_words if WordChecker.is_long(word)]
    print(long_words)