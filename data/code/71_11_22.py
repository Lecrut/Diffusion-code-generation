class ListAnalyzer:
    _EMPTY_ERROR = "List must not be empty"

    def get_middle_value(self, lst):
        if not lst:
            raise ValueError(self._EMPTY_ERROR)
        length = len(lst)
        mid_index = length // 2
        if length % 2 == 0:
            return lst[mid_index]
        return lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    result = analyzer.get_middle_value(sample_list)
    print(result)
    sample_list_even = [100, 200, 300, 400]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)