class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def compare(self, a, b):
        if a > b:
            return f"{a} is greater than {b}"
        elif a < b:
            return f"{a} is less than {b}"
        else:
            return f"{a} is equal to {b}"

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(50, 30))
    print(calculator.compare(75, 100))
    print(calculator.compare(25, 25))