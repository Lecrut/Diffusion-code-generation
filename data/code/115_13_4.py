from decimal import Decimal, getcontext

def divide_decimals():
    getcontext().prec = 50
    result = Decimal('1') / Decimal('3')
    return result
if __name__ == '__main__':
    print(divide_decimals())