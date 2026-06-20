class SumCalculator:
    @staticmethod
    def sum_three_numbers(a, b, c):
        return a + b + c

if __name__ == '__main__':
    result = SumCalculator.sum_three_numbers(10, 20, 30)
    print(result)