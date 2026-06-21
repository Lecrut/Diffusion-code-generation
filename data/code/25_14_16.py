from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price():
    original_price = Decimal("100.00")
    discount_percentage = Decimal("15.00")

    discount_amount = original_price * (discount_percentage / Decimal("100"))
    discounted_price = original_price - discount_amount

    return discounted_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = calculate_discounted_price()
    print(result)