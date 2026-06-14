import math
class ListAnalyzer:
    def __init__(self, data=None):
        if data is None:
            self._data = []
        elif isinstance(data, list):
            self._data = data
        else:
            self._data = []
    def get_maximum(self):
        if not self._data:
            return -math.inf
        return max(self._data)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    analyzer1 = ListAnalyzer(list1)
    print(f"Maximum of {list1}: {analyzer1.get_maximum()}")
    list2 = [-10, -5, -20, -1]
    analyzer2 = ListAnalyzer(list2)
    print(f"Maximum of {list2}: {analyzer2.get_maximum()}")
    list3 = []
    analyzer3 = ListAnalyzer(list3)
    print(f"Maximum of {list3}: {analyzer3.get_maximum()}")
    list4 = [42]
    analyzer4 = ListAnalyzer(list4)
    print(f"Maximum of {list4}: {analyzer4.get_maximum()}")