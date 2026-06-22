class SumCalculator:
    @staticmethod
    def sum_three(a, b, c):
        return a + b + c

if __name__ == '__main__':
    result = SumCalculator.sum_three(10, 25, 30)
    print(result)