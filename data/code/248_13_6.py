class SumCalculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

if __name__ == '__main__':
    result = SumCalculator.add(7, 9)
    print(result)