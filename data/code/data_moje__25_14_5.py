from decimal import Decimal, ROUND_HALF_UP

DISCOUNT_RATE = Decimal("0.15")
ITEM_PRICE = Decimal("129.99")

def calculate_discounted_price(price: Decimal, rate: Decimal) -> Decimal:
    discount_amount = price * rate
    discounted_value = price - discount_amount
    return discounted_value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    result = calculate_discounted_price(ITEM_PRICE, DISCOUNT_RATE)
    print(result)