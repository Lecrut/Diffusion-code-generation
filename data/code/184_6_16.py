class BinarySearch:
    def __init__(self):
        self.words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

    def search(self, keyword):
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
    print(search_instance.search('kiwi'))
    print(search_instance.search('apple'))