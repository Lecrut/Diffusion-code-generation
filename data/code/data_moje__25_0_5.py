def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if not isinstance(original_price, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Both inputs must be numeric")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discounted_price = original_price * (1 - discount_percentage / 100)
    return round(discounted_price, 2)

if __name__ == '__main__':
    original = 100.00
    discount = 20.0
    result = calculate_discounted_price(original, discount)
    print(result)