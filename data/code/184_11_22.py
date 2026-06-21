class TextKeywordChecker:
    def __init__(self, text):
        self.text = text

    def check_keyword(self, keyword):
        return keyword in self.text

if __name__ == '__main__':
    searcher = TextKeywordChecker("This is a sample text for testing.")
    print(searcher.check_keyword("sample"))
    print(searcher.check_keyword("missing"))