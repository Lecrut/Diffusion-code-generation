import decimal

def convert_dollars_to_cents(dollars):
    d = decimal.Decimal(str(dollars))
    result = d * 100
    return int(result)

if __name__ == '__main__':
    val1 = 10.50
    val2 = 0.01
    val3 = 100.005
    print(convert_dollars_to_cents(val1))
    print(convert_dollars_to_cents(val2))
    print(convert_dollars_to_cents(val3))