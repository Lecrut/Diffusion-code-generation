class BinarySearch:
    WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

    def search(self, keyword):
        low = 0
        high = len(self.WORDS) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.WORDS[mid] == keyword:
                return True
            elif self.WORDS[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    search_instance = BinarySearch()
    print(search_instance.search('cherry'))