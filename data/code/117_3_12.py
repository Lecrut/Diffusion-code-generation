from decimal import Decimal

def calculate_monetary_difference(value1: Decimal, value2: Decimal) -> Decimal:
    return value1 - value2

if __name__ == '__main__':
    sample_values = {
        'amount_a': Decimal('10.50'),
        'amount_b': Decimal('3.25')
    }
    
    result = calculate_monetary_difference(sample_values['amount_a'], sample_values['amount_b'])
    print(result)