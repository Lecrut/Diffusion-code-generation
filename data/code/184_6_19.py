class KeywordSearch:
    def __init__(self):
        self.keywords = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    def find_keyword(self, keyword):
        low = 0
        high = len(self.keywords) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.keywords[mid] == keyword:
                return True
            elif self.keywords[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    search_instance = KeywordSearch()
    target_keyword = 'banana'
    print(search_instance.find_keyword(target_keyword))