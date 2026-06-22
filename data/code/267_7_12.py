class WordLengthChecker:

    def __init__(self, max_length=10):
        self.max_length = max_length

    def is_long(self, word):
        return len(word) > self.max_length
if __name__ == '__main__':
    checker = WordLengthChecker(10)
    print(checker.is_long('short'))
    print(checker.is_long('this is too long'))