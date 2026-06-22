import decimal

def convert_dollars_to_cents(dollar_value):
    if isinstance(dollar_value, str):
        dollar_decimal = decimal.Decimal(dollar_value)
    else:
        dollar_decimal = decimal.Decimal(str(dollar_value))
    
    cents_value = dollar_decimal * decimal.Decimal('100')
    return cents_value

if __name__ == '__main__':
    sample_values = ['10.00', '19.99', '0.01', '100', '12.345']
    for val in sample_values:
        result = convert_dollars_to_cents(val)
        print(result)