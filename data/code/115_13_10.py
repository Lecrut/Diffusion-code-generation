from decimal import Decimal, getcontext

def divide_decimals():
    getcontext().prec = 50
    num1 = Decimal('1.23456789012345678901234567890123456789012345678')
    num2 = Decimal('0.123456789012345678901234567890123456789012345678')
    result = num1 / num2
    return result
if __name__ == '__main__':
    print(divide_decimals())