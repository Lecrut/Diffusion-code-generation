import decimal

decimal.getcontext().prec = 20

def calculate_discounted_price(original_price, discount_percentage):
    price = decimal.Decimal(str(original_price))
    discount = decimal.Decimal(str(discount_percentage))
    discount_amount = price * discount / decimal.Decimal('100')
    final_price = price - discount_amount
    return final_price.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)

if __name__ == '__main__':
    sample_price = 199.99
    sample_discount = 25
    result = calculate_discounted_price(sample_price, sample_discount)
    print(result)