class WordLengthChecker:
    def __init__(self, words):
        self.words = words

    def has_long_word(self):
        for word in self.words:
            if len(word) > 7:
                return True
        return False

if __name__ == '__main__':
    checker = WordLengthChecker(["apple", "banana", "cherry", "date"])
    print(checker.has_long_word())