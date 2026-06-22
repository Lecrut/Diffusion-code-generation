class SumCalculator:
    @staticmethod
    def sum_two_numbers(a, b):
        return a + b

if __name__ == '__main__':
    result1 = SumCalculator.sum_two_numbers(3, 5)
    print(result1)
    result2 = SumCalculator.sum_two_numbers(7, 9)
    print(result2)