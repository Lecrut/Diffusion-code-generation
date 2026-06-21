from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price, discount_rate):
    price = Decimal(str(original_price))
    rate = Decimal(str(discount_rate))
    discount_amount = price * rate
    discounted = price - discount_amount
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    original = 99.99
    discount = 0.25
    result = calculate_discounted_price(original, discount)
    print(result)