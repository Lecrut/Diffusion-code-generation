class WordSearcher:
    def __init__(self, words):
        self.words = words

    def contains_word(self, word):
        return any(w == word for w in self.words)

if __name__ == '__main__':
    searcher = WordSearcher(["apple", "banana", "cherry"])
    print(searcher.contains_word("banana"))
    print(searcher.contains_word("grape"))