class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if a > b:
            return 'Greater'
        elif a < b:
            return 'Less'
        else:
            return 'Equal'
if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(50, 30))
    print(calculator.compare(20, 40))
    print(calculator.compare(10, 10))