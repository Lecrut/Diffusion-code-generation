class KeywordSearcher:
    def __init__(self, tokens):
        self.tokens = sorted(tokens)

    def binary_search_keyword(self, keyword):
        left, right = 0, len(self.tokens) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.tokens[mid] == keyword:
                return True
            elif self.tokens[mid] < keyword:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':
    searcher = KeywordSearcher(['apple', 'banana', 'cherry', 'date', 'elderberry'])
    print(searcher.binary_search_keyword('banana'))
    print(searcher.binary_search_keyword('grape'))