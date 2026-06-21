class SubstringSearcher:
    def __init__(self, corpus):
        self.corpus = corpus

    def contains_substring(self, substring):
        return self.corpus.find(substring) != -1

if __name__ == '__main__':
    searcher = SubstringSearcher("This is a sample text containing the word hello.")
    print(searcher.contains_substring("hello"))
    print(searcher.contains_substring("world"))