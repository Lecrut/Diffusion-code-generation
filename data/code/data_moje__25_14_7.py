from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price, discount_percentage):
    original = Decimal(str(original_price))
    discount = Decimal(str(discount_percentage))
    discounted = original * (1 - discount / Decimal('100'))
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    sample_price = "99.99"
    sample_discount = "20"
    result = calculate_discounted_price(sample_price, sample_discount)
    print(result)