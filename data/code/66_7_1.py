from decimal import Decimal, getcontext

getcontext().prec = 50

def kilometers_to_meters(kilometers):
    value = Decimal(str(kilometers))
    return value * Decimal(1000)

if __name__ == '__main__':
    sample_value = 123.45678901234567890123456789
    result = kilometers_to_meters(sample_value)
    print(result)