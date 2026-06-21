def calculate_discounted_price(original_price: float, discount_percent: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    discount_amount = original_price * (discount_percent / 100.0)
    return original_price - discount_amount

if __name__ == '__main__':
    price = 199.99
    discount = 25.0
    final_price = calculate_discounted_price(price, discount)
    print(final_price)