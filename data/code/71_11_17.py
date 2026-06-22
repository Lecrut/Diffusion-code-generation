class ListAnalyzer:
    _EMPTY_ERROR = "List must not be empty"

    def get_middle_value(self, lst):
        if not lst:
            raise ValueError(self._EMPTY_ERROR)
        length = len(lst)
        return lst[length // 2]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [10, 20, 30, 40, 50]
    result = analyzer.get_middle_value(sample_list)
    print(result)