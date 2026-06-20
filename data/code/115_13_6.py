from decimal import Decimal, getcontext

class DecimalDivider:
    def __init__(self):
        getcontext().prec = 50
    
    def divide(self, num1, num2):
        return num1 / num2

if __name__ == '__main__':
    divider = DecimalDivider()
    result1 = divider.divide(Decimal('1.0'), Decimal('3.0'))
    print(result1)
    
    result2 = divider.divide(Decimal('1.234567890123456789012345678901234567890123456789'), Decimal('2.345678901234567890123456789012345678901234567890'))
    print(result2)
    
    result3 = divider.divide(Decimal('1.234567890123456789012345678901234567890123456789'), Decimal('9.876543210987654321098765432109876543210987654321'))
    print(result3)
    
    result4 = divider.divide(Decimal('1'), Decimal('3'))
    print(result4)