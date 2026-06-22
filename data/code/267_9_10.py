class WordLengthChecker:
    MIN_LENGTH = 8

    @staticmethod
    def is_word_long(word):
        return len(word) > WordLengthChecker.MIN_LENGTH
if __name__ == '__main__':
    checker = WordLengthChecker()
    print(checker.is_word_long('short'))
    print(checker.is_word_long('thisisalongstring'))