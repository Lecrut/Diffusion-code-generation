from decimal import Decimal, getcontext

def precise_division(a, b):
    getcontext().prec = 50
    return Decimal(a) / Decimal(b)
if __name__ == '__main__':
    result = precise_division(1, 3)
    print(result)