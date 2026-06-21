def calculate_price(original_price: float, discount_percent: float) -> tuple:
    discount_amount = original_price * (discount_percent / 100.0)
    final_price = original_price - discount_amount
    return (original_price, discount_amount, final_price)

if __name__ == '__main__':
    original = 99.99
    discount = 30.0
    price, amount, total = calculate_price(original, discount)
    print(price, amount, total)