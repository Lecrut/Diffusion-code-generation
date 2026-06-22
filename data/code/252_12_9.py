class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def compare(self, a, b):
        if a > b:
            return "a is greater than b"
        elif a < b:
            return "a is less than b"
        else:
            return "a is equal to b"

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(50, 30))
    print(calculator.compare(20, 40))
    print(calculator.compare(10, 10))