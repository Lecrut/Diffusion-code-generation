import decimal

def calculate_discounted_price(original_price, discount_rate):
    context = decimal.getcontext()
    context.prec = 28
    price = decimal.Decimal(str(original_price))
    rate = decimal.Decimal(str(discount_rate))
    discount_amount = price * rate
    final_price = price - discount_amount
    return final_price.quantize(decimal.Decimal('0.01'))

if __name__ == '__main__':
    original_price = 199.99
    discount_rate = 0.15
    result = calculate_discounted_price(original_price, discount_rate)
    print(result)