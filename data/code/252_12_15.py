class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if a > b:
            return 'a is greater than b'
        elif a < b:
            return 'a is less than b'
        else:
            return 'a is equal to b'

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    result1 = calculator.compare(50, 30)
    print(result1)
    result2 = calculator.compare(75, 90)
    print(result2)
    result3 = calculator.compare(42, 42)
    print(result3)