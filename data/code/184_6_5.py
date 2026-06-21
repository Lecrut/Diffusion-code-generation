class BinarySearch:
    WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

    @staticmethod
    def search(keyword):
        low = 0
        high = len(BinarySearch.WORDS) - 1
        while low <= high:
            mid = (low + high) // 2
            if BinarySearch.WORDS[mid] == keyword:
                return True
            elif BinarySearch.WORDS[mid] < keyword:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    search_instance = BinarySearch()
    print(search_instance.search('cherry'))