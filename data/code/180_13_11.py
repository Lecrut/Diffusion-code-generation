class WordChecker:
    def __init__(self):
        self.words = {'apple', 'banana', 'cherry'}

    def check_word(self, word):
        return word in self.words

if __name__ == '__main__':
    checker = WordChecker()
    print(checker.check_word('banana'))
    print(checker.check_word('orange'))