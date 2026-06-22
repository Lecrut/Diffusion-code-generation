from decimal import Decimal

def dollars_to_cents(dollar_value):
    decimal_dollars = Decimal(str(dollar_value))
    cents = decimal_dollars * 100
    return cents.to_integral_value()
if __name__ == '__main__':
    test_values = [1.0, 0.01, 123.45, 0.99, 1000.0, '12.34', Decimal('0.01')]
    for value in test_values:
        result = dollars_to_cents(value)
        print(f'{value} dollars = {result} cents')