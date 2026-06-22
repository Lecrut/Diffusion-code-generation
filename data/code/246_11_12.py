import decimal
DECIMAL_PRECISION = 50

def add_two_numbers(a: float, b: float) -> float:
    decimal.getcontext().prec = DECIMAL_PRECISION
    result = decimal.Decimal(str(a)) + decimal.Decimal(str(b))
    return float(result)
if __name__ == '__main__':
    num1 = 0.1
    num2 = 0.2
    result = add_two_numbers(num1, num2)
    print(result)