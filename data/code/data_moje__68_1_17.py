import decimal

def convert_dollars_to_cents(dollar_value):
    d = decimal.Decimal(str(dollar_value))
    cents_value = d * decimal.Decimal('100')
    return cents_value

if __name__ == '__main__':
    sample_values = [10.50, 123.456, 0.99, 1000]
    for val in sample_values:
        result = convert_dollars_to_cents(val)
        print(result)