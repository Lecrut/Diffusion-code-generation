class WordLengthChecker:
    def has_long_word(self, words):
        for word in words:
            if len(word) > 7:
                return True
        return False

if __name__ == '__main__':
    checker = WordLengthChecker()
    sample_words = ["apple", "banana", "cherry", "date"]
    print(checker.has_long_word(sample_words))