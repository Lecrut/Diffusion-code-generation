def calculate_discounted_price(original_price: float, discount_percent: float) -> float:
    if original_price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid input: original_price must be non-negative, discount_percent must be between 0 and 100.")
    discount_amount = original_price * (discount_percent / 100.0)
    final_price = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    original = 100.0
    discount = 20.0
    result = calculate_discounted_price(original, discount)
    print(result)