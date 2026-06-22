class ListAnalyzer:
    def __init__(self, data):
        self._data = list(data)

    def get_middle_element(self):
        n = len(self._data)
        if n == 0:
            return None
        if n % 2 == 1:
            index = n // 2
            return self._data[index]
        else:
            idx1 = n // 2 - 1
            idx2 = n // 2
            val1 = self._data[idx1]
            val2 = self._data[idx2]
            return (val1 + val2) // 2

    def get_length(self):
        return len(self._data)

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [1, 2, 3, 4, 5, 6]
    empty_list = []

    analyzer_odd = ListAnalyzer(odd_list)
    analyzer_even = ListAnalyzer(even_list)
    analyzer_empty = ListAnalyzer(empty_list)

    mid_odd = analyzer_odd.get_middle_element()
    len_odd = analyzer_odd.get_length()
    print(mid_odd)
    print(len_odd)

    mid_even = analyzer_even.get_middle_element()
    len_even = analyzer_even.get_length()
    print(mid_even)
    print(len_even)

    mid_empty = analyzer_empty.get_middle_element()
    print(mid_empty)