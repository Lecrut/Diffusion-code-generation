from decimal import Decimal

def calculate_monetary_difference(amount_a: Decimal, amount_b: Decimal) -> Decimal:
    if not isinstance(amount_a, Decimal) or not isinstance(amount_b, Decimal):
        raise ValueError("Both inputs must be instances of Decimal")
    return amount_a - amount_b

if __name__ == '__main__':
    try:
        sample_value1 = Decimal('10.50')
        sample_value2 = Decimal('3.25')
        result = calculate_monetary_difference(sample_value1, sample_value2)
        print(result)
    except ValueError as e:
        print(e)