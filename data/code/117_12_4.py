from decimal import Decimal

class ValueSubtractor:
    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    subtractor = ValueSubtractor()
    value_a = Decimal('10.50')
    value_b = Decimal('3.25')
    result = subtractor.subtract(value_a, value_b)
    print(result)