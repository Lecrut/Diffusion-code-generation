class ListAnalyzer:
    _EMPTY_ERROR = "List must not be empty"

    @staticmethod
    def _validate_input(lst):
        if not lst:
            raise ValueError(ListAnalyzer._EMPTY_ERROR)
        return len(lst)

    def get_middle_value(self, lst):
        n = self._validate_input(lst)
        mid_index = n // 2
        if n % 2 == 0:
            return lst[mid_index]
        return lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 3, 5, 7, 9]
    result = analyzer.get_middle_value(sample_list)
    print(result)
    sample_list_even = [2, 4, 6, 8]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)