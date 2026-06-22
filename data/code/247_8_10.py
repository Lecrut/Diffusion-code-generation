class SumCalculator:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

if __name__ == '__main__':
    value1 = 10
    value2 = 5
    result = SumCalculator.add_numbers(value1, value2)
    print(result)