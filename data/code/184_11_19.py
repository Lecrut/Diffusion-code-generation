class KeywordSearcher:
    def __init__(self, text):
        self.text = text

    def contains_keyword(self, keyword):
        return keyword in self.text

if __name__ == '__main__':
    searcher = KeywordSearcher("Python is a high-level, interpreted programming language.")
    print(searcher.contains_keyword("interpreted"))
    print(searcher.contains_keyword("missing"))