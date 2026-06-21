class TokenSearcher:
    def __init__(self, tokens):
        self.tokens = sorted(tokens)

    def search_keyword(self, keyword):
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
    searcher = TokenSearcher(['apple', 'banana', 'cherry', 'date', 'elderberry'])
    print(searcher.search_keyword('banana'))
    print(searcher.search_keyword('cherry'))
    print(searcher.search_keyword('grape'))