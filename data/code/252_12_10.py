class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if a > b:
            return 'a is greater than b'
        elif a < b:
            return 'b is greater than a'
        else:
            return 'a is equal to b'

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    result1 = calculator.compare(80, 50)
    print(result1)
    result2 = calculator.compare(30, 45)
    print(result2)
    result3 = calculator.compare(60, 60)
    print(result3)