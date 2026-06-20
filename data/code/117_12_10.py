from decimal import Decimal

class ValueOperations:
    def subtract_values(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    operations = ValueOperations()
    value_a = Decimal('10.50')
    value_b = Decimal('3.25')
    result = operations.subtract_values(value_a, value_b)
    print(result)