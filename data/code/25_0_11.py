def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Price must be non-negative and discount must be between 0 and 100")
    return original_price * (1 - discount_percentage / 100)

if __name__ == '__main__':
    original_price = 100.0
    discount_percentage = 20.0
    final_price = calculate_final_price(original_price, discount_percentage)
    print(final_price)