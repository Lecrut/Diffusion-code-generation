from decimal import Decimal, ROUND_HALF_UP

ORIGINAL_PRICE = Decimal('100.00')
DISCOUNT_PERCENT = Decimal('25')

def calculate_discounted_price(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / Decimal('100'))
    discounted_price = original_price - discount_amount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = calculate_discounted_price(ORIGINAL_PRICE, DISCOUNT_PERCENT)
    print(result)