class TextSearcher:
    def __init__(self, text):
        self.text = text

    def contains_keyword(self, keyword):
        return keyword in self.text

if __name__ == '__main__':
    searcher = TextSearcher("This is a sample text for testing.")
    print(searcher.contains_keyword("sample"))
    print(searcher.contains_keyword("missing"))