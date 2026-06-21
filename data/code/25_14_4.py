from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(price, discount_rate):
    rounded_price = price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    rounded_discount = discount_rate.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    discounted = rounded_price * (Decimal('1') - rounded_discount)
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    sample_price = Decimal('100.00')
    sample_discount = Decimal('0.20')
    result = calculate_discounted_price(sample_price, sample_discount)
    print(result)