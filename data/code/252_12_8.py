class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def validate_inputs(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Inputs must be numbers")
        if a < CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE or a > CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE:
            raise ValueError(f"Value of a ({a}) is out of allowed range [{CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE}, {CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE}]")
        if b < CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE or b > CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE:
            raise ValueError(f"Value of b ({b}) is out of allowed range [{CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE}, {CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE}]")

    @staticmethod
    def compare(a, b):
        CompareTwoSimpleQuantitiesNowCalculator.validate_inputs(a, b)
        if a > b:
            return 'a is greater than b'
        elif a < b:
            return 'a is less than b'
        else:
            return 'a is equal to b'

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    print(calculator.compare(50, 30))
    print(calculator.compare(75, 100))
    print(calculator.compare(25, 25))