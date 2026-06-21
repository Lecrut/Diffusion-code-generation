class NumberSum:
    DEFAULT_NUMBER = 0

    @staticmethod
    def sum_numbers(numbers):
        return sum(numbers) if numbers else NumberSum.DEFAULT_NUMBER

if __name__ == '__main__':
    calculator = NumberSum()
    sample1 = [7, 8, 9]
    sample2 = []
    print(calculator.sum_numbers(sample1))
    print(calculator.sum_numbers(sample2))