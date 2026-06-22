class RangeCycler:
    MIN_VALUE = -10
    MAX_VALUE = 10

    @staticmethod
    def print_positive_numbers(start, end):
        for num in range(max(start, RangeCycler.MIN_VALUE), min(end, RangeCycler.MAX_VALUE) + 1):
            if num > 0:
                print(num)

if __name__ == '__main__':
    RangeCycler.print_positive_numbers(-5, 15)