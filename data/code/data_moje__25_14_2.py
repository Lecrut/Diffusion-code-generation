from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price, discount_rate):
    original_price = Decimal(str(original_price))
    discount_rate = Decimal(str(discount_rate))
    discount_amount = original_price * discount_rate
    discounted_price = original_price - discount_amount
    return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
if __name__ == '__main__':
    sample_price = '99.99'
    sample_discount = '0.15'
    result = calculate_discounted_price(sample_price, sample_discount)
    print(result)