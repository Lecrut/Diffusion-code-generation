def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if original_price < 0 or discount_percentage < 0:
        raise ValueError("Price and discount percentage cannot be negative")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100")
    discount_amount = original_price * (discount_percentage / 100.0)
    final_price = original_price - discount_amount
    return round(final_price, 2)

if __name__ == '__main__':
    original = 199.99
    discount = 25.0
    result = calculate_discounted_price(original, discount)
    print(result)