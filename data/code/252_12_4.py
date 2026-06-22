class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if a > b:
            return "a is greater than b"
        elif a < b:
            return "a is less than b"
        else:
            return "a is equal to b"

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(10, 20))
    print(calculator.compare(30, 15))
    print(calculator.compare(40, 40))