class ListAnalyzer:
    _ODD_OFFSET = 0
    _EVEN_OFFSET = 1

    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        length = len(lst)
        if length % 2 == 1:
            return lst[length // 2]
        return lst[length // 2 + self._EVEN_OFFSET]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list_odd = [10, 20, 30, 40, 50]
    result_odd = analyzer.get_middle_value(sample_list_odd)
    print(result_odd)
    sample_list_even = [10, 20, 30, 40]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)