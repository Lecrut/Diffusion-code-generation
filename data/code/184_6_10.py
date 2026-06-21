class BinarySearch:
    def __init__(self):
        self.words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

    def is_valid_keyword(self, keyword):
        return isinstance(keyword, str) and keyword.isalpha()

    def search(self, keyword):
        if not self.is_valid_keyword(keyword):
            raise ValueError("Invalid keyword. Must be a non-empty alphabetic string.")
        
        low = 0
        high = len(self.words) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.words[mid] == keyword:
                return True
            elif self.words[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    search_instance = BinarySearch()
    print(search_instance.search('cherry'))