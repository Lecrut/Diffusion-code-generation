class TextSearcher:
    DEFAULT_TEXT = "This is a sample text for testing."

    @staticmethod
    def contains_keyword(text, keyword):
        return keyword in text

if __name__ == '__main__':
    searcher = TextSearcher()
    print(searcher.contains_keyword(TextSearcher.DEFAULT_TEXT, "sample"))
    print(searcher.contains_keyword(TextSearcher.DEFAULT_TEXT, "missing"))