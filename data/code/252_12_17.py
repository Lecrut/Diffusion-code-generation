class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if a > b:
            return f'{a} is greater than {b}'
        elif a < b:
            return f'{a} is less than {b}'
        else:
            return f'{a} is equal to {b}'

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    result1 = calculator.compare(50, 30)
    result2 = calculator.compare(75, 90)
    result3 = calculator.compare(45, 45)
    print(result1)
    print(result2)
    print(result3)