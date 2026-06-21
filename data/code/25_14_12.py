from decimal import Decimal, ROUND_HALF_UP

DISCOUNT_RATE = Decimal("0.15")
BASE_PRICE = Decimal("199.99")

def calculate_discounted_price(price, rate):
    discount_amount = price * rate
    final_price = price - discount_amount
    return final_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    result = calculate_discounted_price(BASE_PRICE, DISCOUNT_RATE)
    print(result)