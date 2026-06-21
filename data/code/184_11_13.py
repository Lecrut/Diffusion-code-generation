class KeywordSearcher:
    def __init__(self, document):
        self.document = document

    def search(self, keyword):
        return keyword in self.document

if __name__ == '__main__':
    searcher = KeywordSearcher("This is a sample text for testing.")
    print(searcher.search("sample"))
    print(searcher.search("missing"))