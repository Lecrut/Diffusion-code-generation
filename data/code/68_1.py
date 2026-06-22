import decimal

def convert_dollars_to_cents(dollar_value):
    d = decimal.Decimal(str(dollar_value))
    cents = d * 100
    return cents

if __name__ == '__main__':
    test_values = ['10.5', '0.01', '123.456', '0', '-5.99']
    for val in test_values:
        result = convert_dollars_to_cents(val)
        print(result)