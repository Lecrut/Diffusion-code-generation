class WordSearcher:
    def __init__(self, words):
        self.word_set = set(word.lower() for word in words)

    def is_word_present(self, word):
        return word.lower() in self.word_set

if __name__ == '__main__':
    searcher = WordSearcher(["apple", "banana", "cherry"])
    print(f"'Apple' in list: {searcher.is_word_present('Apple')}")
    print(f"'Banana' in list: {searcher.is_word_present('Banana')}")
    print(f"'Cherry' in list: {searcher.is_word_present('Cherry')}")
    print(f"'Orange' in list: {searcher.is_word_present('Orange')}")