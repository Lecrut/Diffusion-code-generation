from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(price, discount_rate):
    discount = Decimal(str(price)) * Decimal(str(discount_rate))
    discounted_price = Decimal(str(price)) - discount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    original_price = 100
    discount_rate = 0.15
    result = calculate_discounted_price(original_price, discount_rate)
    print(result)