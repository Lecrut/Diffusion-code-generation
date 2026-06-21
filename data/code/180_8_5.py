class WordSearcher:

    def __init__(self, collection):
        self.collection = collection

    def contains_word(self, word):
        return any((word == item for item in self.collection))
if __name__ == '__main__':
    searcher = WordSearcher(['world', 'python', 'hello', 'programming'])
    print(searcher.contains_word('hello'))
    print(searcher.contains_word('code'))