class SumCalculator:
    @staticmethod
    def calculate_sum(a, b, c):
        return a + b + c

if __name__ == '__main__':
    num1 = 10
    num2 = 20
    num3 = 30
    result = SumCalculator.calculate_sum(num1, num2, num3)
    print(result)