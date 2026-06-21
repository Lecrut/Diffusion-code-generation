from decimal import Decimal, ROUND_HALF_UP

ORIG_PRICE = Decimal('100.00')
DISCOUNT_PERCENT = Decimal('20')

def calculate_discounted_price(orig_price, discount_percent):
    discount_amount = orig_price * (discount_percent / Decimal('100'))
    discounted_price = orig_price - discount_amount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = calculate_discounted_price(ORIG_PRICE, DISCOUNT_PERCENT)
    print(result)