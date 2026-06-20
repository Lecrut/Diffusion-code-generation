from decimal import Decimal, getcontext

def divide_decimals():
    getcontext().prec = 50
    a = Decimal('1.0')
    b = Decimal('3.0')
    result = a / b
    return result
if __name__ == '__main__':
    print(divide_decimals())