class WordSearcher:
    def __init__(self, sequence):
        self.sequence = sequence

    def contains_word(self, target):
        return any(word == target for word in self.sequence)

if __name__ == '__main__':
    searcher = WordSearcher(['apple', 'banana', 'cherry'])
    print(searcher.contains_word('banana'))
    print(searcher.contains_word('grape'))