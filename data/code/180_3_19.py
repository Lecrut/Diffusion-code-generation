class KeywordSearcher:
    @staticmethod
    def binary_search(keyword, tokens):
        left, right = 0, len(tokens) - 1
        while left <= right:
            mid = (left + right) // 2
            if tokens[mid] == keyword:
                return True
            elif tokens[mid] < keyword:
                left = mid + 1
            else:
                right = mid - 1
        return False

    @classmethod
    def search_keyword(cls, sample_tokens, sample_keyword):
        sample_tokens.sort()
        return cls.binary_search(sample_keyword, sample_tokens)

if __name__ == '__main__':
    sample_tokens = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    sample_keyword = 'cherry'
    print(KeywordSearcher.search_keyword(sample_tokens, sample_keyword))