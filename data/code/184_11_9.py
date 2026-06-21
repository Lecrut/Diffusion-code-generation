class KeywordSearcher:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def validate_input(keyword):
        if not isinstance(keyword, str):
            raise ValueError("Keyword must be a string")

    def contains_keyword(self, keyword):
        self.validate_input(keyword)
        return keyword in self.text

if __name__ == '__main__':
    searcher = KeywordSearcher("This is a sample text for testing.")
    print(searcher.contains_keyword("sample"))
    print(searcher.contains_keyword("missing"))