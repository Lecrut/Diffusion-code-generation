from decimal import Decimal, getcontext

def divide_numbers():
    getcontext().prec = 50
    num1 = Decimal('1.234567890123456789012345678901234567890123456789')
    num2 = Decimal('2.34567890123456789012345678901234567890123456789')
    result = num1 / num2
    return result
if __name__ == '__main__':
    print(divide_numbers())