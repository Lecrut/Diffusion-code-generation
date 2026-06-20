import decimal
MAX_PRECISION = 50

def multiply_numbers(a, b):
    decimal.getcontext().prec = MAX_PRECISION
    result = decimal.Decimal(a) * decimal.Decimal(b)
    return result
if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = multiply_numbers(num1, num2)
    print(result)