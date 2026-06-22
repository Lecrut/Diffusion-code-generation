class ListAnalyzer:
    _ZERO = 0
    _TWO = 2

    @staticmethod
    def _validate(lst):
        if len(lst) == ListAnalyzer._ZERO:
            raise ValueError("List cannot be empty")

    def get_middle_value(self, lst):
        self._validate(lst)
        n = len(lst)
        if n % ListAnalyzer._TWO == 1:
            return lst[n // ListAnalyzer._TWO]
        mid = n // ListAnalyzer._TWO
        return (lst[mid - 1] + lst[mid]) / ListAnalyzer._TWO

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    odd_list = [10, 20, 30, 40, 50]
    even_list = [1, 3, 5, 7]
    print(analyzer.get_middle_value(odd_list))
    print(analyzer.get_middle_value(even_list))