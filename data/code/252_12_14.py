class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def compare(self, a, b):
        if a > b:
            return "A is greater than B"
        elif a < b:
            return "A is less than B"
        else:
            return "A is equal to B"

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(50, 30))
    print(calculator.compare(20, 40))
    print(calculator.compare(10, 10))