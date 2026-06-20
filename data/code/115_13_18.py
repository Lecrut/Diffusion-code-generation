from decimal import Decimal, getcontext

def divide_decimals():
    getcontext().prec = 50
    a = Decimal('1.234567890123456789012345678901234567890123456789')
    b = Decimal('9.876543210987654321098765432109876543210987654321')
    result = a / b
    return result
if __name__ == '__main__':
    print(divide_decimals())