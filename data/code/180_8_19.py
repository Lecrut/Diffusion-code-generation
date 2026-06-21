class WordFinder:
    def __init__(self, collection):
        self.collection = collection

    def is_word_present(self, word):
        return any(word == item for item in self.collection)

if __name__ == '__main__':
    finder = WordFinder(['world', 'python', 'hello', 'programming'])
    print(finder.is_word_present('hello'))
    print(finder.is_word_present('code'))