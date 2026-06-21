def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Inputs must be numeric")
    if original_price < 0 or discount_percentage < 0:
        raise ValueError("Inputs must be non-negative")
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot exceed 100")
    return original_price * (1 - discount_percentage / 100)

if __name__ == '__main__':
    original_price = 100.0
    discount_percentage = 20.0
    result = calculate_discounted_price(original_price, discount_percentage)
    print(result)