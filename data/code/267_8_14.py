class WordLengthChecker:

    def is_word_long(self, word):
        return len(word) > 5
if __name__ == '__main__':
    checker = WordLengthChecker()
    print(checker.is_word_long('hello'))
    print(checker.is_word_long('world'))
    print(checker.is_word_long('Python'))