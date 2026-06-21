from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price, discount_percentage):
    price = Decimal(str(original_price))
    discount = Decimal(str(discount_percentage)) / Decimal('100')
    discounted = price * (Decimal('1') - discount)
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    original = Decimal('99.99')
    discount = Decimal('15.5')
    result = calculate_discounted_price(original, discount)
    print(result)