from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(original_price: float, discount_rate: float) -> str:
    price = Decimal(str(original_price))
    rate = Decimal(str(discount_rate))
    discount_amount = price * rate / Decimal('100')
    discounted = price - discount_amount
    return str(discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    result = calculate_discounted_price(100.0, 15)
    print(result)