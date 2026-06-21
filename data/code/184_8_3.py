class WordSearcher:

    def __init__(self, sequence):
        self.sequence = sequence

    def contains_word(self, target):
        return any((word == target for word in self.sequence))
if __name__ == '__main__':
    searcher1 = WordSearcher(['apple', 'banana', 'cherry'])
    print(searcher1.contains_word('banana'))
    print(searcher1.contains_word('grape'))
    searcher2 = WordSearcher(['dog', 'cat', 'mouse'])
    print(searcher2.contains_word('cat'))
    print(searcher2.contains_word('bird'))