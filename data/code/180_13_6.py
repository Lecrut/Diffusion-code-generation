class WordChecker:
    def __init__(self):
        self.predefined_words = {'apple', 'banana', 'cherry'}

    def word_exists(self, word):
        return word.lower() in self.predefined_words

if __name__ == '__main__':
    checker = WordChecker()
    print(checker.word_exists('Banana'))
    print(checker.word_exists('grape'))