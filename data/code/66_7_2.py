import decimal

def kilometers_to_meters(kilometers):
    km = decimal.Decimal(str(kilometers))
    return (km * decimal.Decimal('1000')).to_integral_value()

if __name__ == '__main__':
    result = kilometers_to_meters(1.23456789)
    print(result)