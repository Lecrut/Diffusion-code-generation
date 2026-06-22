class CompareTwoSimpleQuantitiesNowCalculator:
    MIN_VALUE = 0
    MAX_VALUE = 100

    @staticmethod
    def compare(a, b):
        if a < b:
            return 'a is less than b'
        elif a > b:
            return 'a is greater than b'
        else:
            return 'a is equal to b'
if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(10, 20))
    print(calculator.compare(30, 20))
    print(calculator.compare(25, 25))