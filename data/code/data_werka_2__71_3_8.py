class ListAnalyzer:
    _DEFAULT_EMPTY_RESULT = None

    def __init__(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        self._items = list(data)

    @staticmethod
    def _compute_index(length):
        if length == 0:
            return -1
        return (length - 1) // 2

    def get_middle_value(self):
        count = len(self._items)
        if count == 0:
            return self._DEFAULT_EMPTY_RESULT
        idx = self._compute_index(count)
        return self._items[idx]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.get_middle_value())

    sample_list2 = [100]
    analyzer2 = ListAnalyzer(sample_list2)
    print(analyzer2.get_middle_value())

    sample_list3 = [5, 15, 25, 35, 45, 55]
    analyzer3 = ListAnalyzer(sample_list3)
    print(analyzer3.get_middle_value())