class SumCalculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

if __name__ == '__main__':
    x = 7
    y = 9
    result = SumCalculator.add(x, y)
    print(result)