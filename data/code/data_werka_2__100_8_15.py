class NumberComparator:
    ZERO = 0
    ONE = 1

    @staticmethod
    def _validate_numeric(value):
        if isinstance(value, bool):
            raise ValueError("Boolean inputs are not supported")
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be numeric")
        return value

    def __init__(self, first, second):
        self._first = self._validate_numeric(first)
        self._second = self._validate_numeric(second)

    def get_sum(self):
        return self._first + self._second

    def get_difference(self):
        return self._first - self._second

    def is_sum_greater_than_difference(self):
        current_sum = self.get_sum()
        current_diff = self.get_difference()
        return current_sum > current_diff

def run_comparison():
    num_a = 10
    num_b = 5
    comparator = NumberComparator(num_a, num_b)
    result = comparator.is_sum_greater_than_difference()
    print(result)

if __name__ == '__main__':
    run_comparison()