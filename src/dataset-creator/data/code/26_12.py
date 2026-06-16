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
    print(f"After adding 'apple': {wd.words}")
    wd.add_word("banana")
    print(f"After adding 'banana': {wd.words}")
    wd.add_word("apple")
    print(f"After adding duplicate 'apple': {wd.words}")
    wd.add_word("")
    print(f"After adding empty string: {wd.words}")
    wd.add_word("orange")
    print(f"After adding 'orange': {wd.words}")