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
    result1 = calculator.compare(75, 25)
    result2 = calculator.compare(40, 60)
    result3 = calculator.compare(80, 80)
    print(result1)
    print(result2)
    print(result3)