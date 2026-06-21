class BinarySearchKeyword:
    @staticmethod
    def binary_search(keyword, tokens):
        tokens.sort()
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

    @staticmethod
    def main():
        sample_tokens = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        search_keyword = 'banana'
        result = BinarySearchKeyword.binary_search(search_keyword, sample_tokens)
        print(result)

if __name__ == '__main__':
    BinarySearchKeyword.main()