class WordDictionary:
    def __init__(self):
        self.words = set()
    def add_word(self, word):
        if word and word not in self.words:
            self.words.add(word)
if __name__ == '__main__':
    wd = WordDictionary()
    print(f"Initial dictionary: {wd.words}")
    wd.add_word("apple")
    wd.add_word("banana")
    wd.add_word("apple")
    wd.add_word("")
    wd.add_word("cherry")
    print(f"Dictionary after adding words: {wd.words}")