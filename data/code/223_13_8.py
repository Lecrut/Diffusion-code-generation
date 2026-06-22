class ListAnalyzer:
    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = list(data)
    
    def get_maximum(self):
        if not self._data:
            return -float('inf')
        return max(self._data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    analyzer1 = ListAnalyzer(list1)
    print(f"Maximum of {list1}: {analyzer1.get_maximum()}")
    
    list2 = [-10, -5, -20, -1]
    analyzer2 = ListAnalyzer(list2)
    print(f"Maximum of {list2}: {analyzer2.get_maximum()}")