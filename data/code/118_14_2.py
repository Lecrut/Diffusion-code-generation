from decimal import Decimal

def multiply_decimals(a: Decimal, b: Decimal) -> Decimal:
    return a * b

if __name__ == '__main__':
    values = {
        'factor1': Decimal('10.5'),
        'factor2': Decimal('2.3')
    }
    result = multiply_decimals(values['factor1'], values['factor2'])
    print(result)