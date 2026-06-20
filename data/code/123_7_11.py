class RangeSum:
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end

    @staticmethod
    def sum_even_numbers(start, end):
        return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    calculator = RangeSum(1, 10)
    print(calculator.sum_even_numbers())