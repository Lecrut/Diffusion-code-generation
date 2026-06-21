from decimal import Decimal, ROUND_HALF_UP

DISCOUNT_RATE = Decimal("0.20")
ITEM_PRICE = Decimal("49.99")

def calculate_discounted_price(price: Decimal, discount: Decimal) -> Decimal:
    discount_amount = price * discount
    final_price = price - discount_amount
    return final_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    result = calculate_discounted_price(ITEM_PRICE, DISCOUNT_RATE)
    print(result)