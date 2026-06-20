from decimal import Decimal, getcontext

def divide_numbers():
    getcontext().prec = 50
    num1 = Decimal('1.0')
    num2 = Decimal('3.0')
    result = num1 / num2
    return result
if __name__ == '__main__':
    print(divide_numbers())