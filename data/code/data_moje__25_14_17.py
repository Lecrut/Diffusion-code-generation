from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price: Decimal, discount_percent: Decimal) -> Decimal:
    discount_amount = original_price * (discount_percent / Decimal('100'))
    discounted_price = original_price - discount_amount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    original = Decimal('100.00')
    discount = Decimal('15.50')
    result = calculate_discounted_price(original, discount)
    print(result)