class BinarySearch:

    def __init__(self, words):
        self.words = sorted(words)

    def search(self, keyword):
        low, high = (0, len(self.words) - 1)
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
    search_instance = BinarySearch(['apple', 'banana', 'cherry', 'date', 'elderberry'])
    print(search_instance.search('banana'))
    print(search_instance.search('grape'))