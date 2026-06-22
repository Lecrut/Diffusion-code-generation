class ListAnalyzer:
    DEFAULT_MAX = -math.inf

    def __init__(self, data=None):
        self._data = list(data) if data is not None else []

    @staticmethod
    def find_max(values):
        return max(values, default=ListAnalyzer.DEFAULT_MAX)

    def get_maximum(self):
        return ListAnalyzer.find_max(self._data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    analyzer1 = ListAnalyzer(list1)
    print(f"Maximum of {list1}: {analyzer1.get_maximum()}")

    list2 = [-10, -5, -20, -1]
    analyzer2 = ListAnalyzer(list2)
    print(f"Maximum of {list2}: {analyzer2.get_maximum()}")