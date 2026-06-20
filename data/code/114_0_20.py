from decimal import Decimal

def multiply_numbers(a, b):
    return Decimal(a) * Decimal(b)

if __name__ == '__main__':
    pi = Decimal('3.141592653589793')
    e = Decimal('2.718281828459045')
    result = multiply_numbers(pi, e)
    print(result)