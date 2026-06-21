from decimal import Decimal, ROUND_HALF_UP

ORIGINAL_PRICE = Decimal('100.00')
DISCOUNT_PERCENT = Decimal('15')

def calculate_discounted_price(price, discount_percent):
    discount_amount = price * (discount_percent / Decimal('100'))
    discounted = price - discount_amount
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = calculate_discounted_price(ORIGINAL_PRICE, DISCOUNT_PERCENT)
    print(result)