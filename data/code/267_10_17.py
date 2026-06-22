class WordChecker:
    def __init__(self, min_length=5):
        self.min_length = min_length

    def is_word_long(self, word):
        return len(word) >= self.min_length

if __name__ == '__main__':
    checker = WordChecker()
    print(checker.is_word_long("short"))
    print(checker.is_word_long("longerword"))