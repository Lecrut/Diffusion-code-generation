class RangeSum:
    START = 1
    END = 10

    @staticmethod
    def sum_even_numbers(start=START, end=END):
        return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    calculator = RangeSum()
    print(calculator.sum_even_numbers())