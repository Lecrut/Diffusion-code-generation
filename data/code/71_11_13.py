class ListAnalyzer:
    _EMPTY_ERROR = "List must not be empty"

    def get_middle_value(self, lst):
        if not lst:
            raise ValueError(self._EMPTY_ERROR)
        return lst[len(lst) >> 1]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    data = [5, 10, 15, 20, 25, 30, 35]
    print(analyzer.get_middle_value(data))