class SumCalculator:
    @staticmethod
    def sum_numbers(a, b):
        return a + b

if __name__ == '__main__':
    calc = SumCalculator()
    result1 = calc.sum_numbers(3, 5)
    print(result1)
    result2 = calc.sum_numbers(7, 9)
    print(result2)