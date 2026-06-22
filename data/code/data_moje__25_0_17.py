def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_factor = 1.0 - (discount_percentage / 100.0)
    return original_price * discount_factor

if __name__ == '__main__':
    sample_original_price = 100.0
    sample_discount_percentage = 20.0
    result = calculate_discounted_price(sample_original_price, sample_discount_percentage)
    print(result)