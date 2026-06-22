from decimal import Decimal, getcontext

def kilometers_to_meters(kilometers):
    getcontext().prec = 28
    km = Decimal(str(kilometers))
    return km * Decimal('1000')

if __name__ == '__main__':
    result = kilometers_to_meters(5.23)
    print(result)
    result2 = kilometers_to_meters(0.001)
    print(result2)
    result3 = kilometers_to_meters(123456.789)
    print(result3)