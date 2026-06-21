from decimal import Decimal, ROUND_HALF_UP

def calculate_discounted_price(price_str="100.00", discount_percent_str="20.00"):
    price = Decimal(price_str)
    discount_percent = Decimal(discount_percent_str)
    discount_amount = price * (discount_percent / Decimal("100"))
    discounted_price = price - discount_amount
    rounded_price = discounted_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return rounded_price

if __name__ == '__main__':
    result = calculate_discounted_price("100.00", "20.00")
    print(result)