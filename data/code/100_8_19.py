class NumberComparator:
    _ZERO = 0
    _ONE = 1

    @staticmethod
    def _get_sum(first, second):
        return first + second

    @staticmethod
    def _get_difference(first, second):
        return first - second

    def compare_sum_and_difference(self, first, second):
        sum_val = self._get_sum(first, second)
        diff_val = self._get_difference(first, second)
        return sum_val > diff_val

if __name__ == '__main__':
    comp = NumberComparator()
    x = 10
    y = 5
    result = comp.compare_sum_and_difference(x, y)
    print(result)