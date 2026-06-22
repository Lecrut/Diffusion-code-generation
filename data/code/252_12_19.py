class CompareTwoSimpleQuantitiesNowCalculator:
    MAX_VALUE = 100
    MIN_VALUE = 0

    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, (int, float)) or quantity < CompareTwoSimpleQuantitiesNowCalculator.MIN_VALUE or quantity > CompareTwoSimpleQuantitiesNowCalculator.MAX_VALUE:
            raise ValueError("Quantity must be a number between 0 and 100")

    @staticmethod
    def compare(a, b):
        CompareTwoSimpleQuantitiesNowCalculator.validate_quantity(a)
        CompareTwoSimpleQuantitiesNowCalculator.validate_quantity(b)

        if a > b:
            return 'a is greater than b'
        elif a < b:
            return 'a is less than b'
        else:
            return 'a is equal to b'

if __name__ == '__main__':
    calculator = CompareTwoSimpleQuantitiesNowCalculator()
    result = calculator.compare(50, 30)
    print(result)