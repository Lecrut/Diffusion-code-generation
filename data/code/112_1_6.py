import decimal

DECIMAL_PLACES = 15

def add_two_numbers(a, b):
    return round(decimal.Decimal(str(a)) + decimal.Decimal(str(b)), DECIMAL_PLACES)

if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = add_two_numbers(num1, num2)
    print(result)