class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def compare(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError('Both inputs must be numbers')
        if a < CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE or a > CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE:
            raise ValueError(f'a must be between {CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE} and {CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE}')
        if b < CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE or b > CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE:
            raise ValueError(f'b must be between {CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE} and {CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE}')
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
    result2 = calculator.compare(30, 45)
    print(result2)
    result3 = calculator.compare(60, 60)
    print(result3)