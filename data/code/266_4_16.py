class UniqueWordCounter:
    def __init__(self):
        self.unique_words = set()

    def add_word(self, word):
        self.unique_words.add(word.lower())

    def count_unique_words(self):
        return len(self.unique_words)

if __name__ == '__main__':
    counter = UniqueWordCounter()
    counter.add_word("hello")
    counter.add_word("world")
    counter.add_word("hello")
    counter.add_word("Python")
    print(counter.count_unique_words())