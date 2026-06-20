from decimal import Decimal, getcontext

def perform_division():
    getcontext().prec = 50
    dividend = Decimal('123456789.123456789')
    divisor = Decimal('987654321.987654321')
    quotient = dividend / divisor
    return quotient

if __name__ == '__main__':
    result = perform_division()
    print(result)