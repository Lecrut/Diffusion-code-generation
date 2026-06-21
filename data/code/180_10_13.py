class WordSearcher:
    def __init__(self, word_list):
        self.word_set = set(word.lower() for word in word_list)

    def is_word_present(self, word):
        return word.lower() in self.word_set

if __name__ == '__main__':
    searcher = WordSearcher(["Hello", "World", "Python", "Programming"])
    print(f"'world' in list: {searcher.is_word_present('world')}")
    print(f"'python' in list: {searcher.is_word_present('python')}")
    print(f"'case' in list: {searcher.is_word_present('case')}")
    print(f"'missing' in list: {searcher.is_word_present('missing')}")