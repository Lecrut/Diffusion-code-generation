def calculate_final_price(original_price, discount_percentage):
    if not isinstance(original_price, (int, float)):
        raise TypeError("Original price must be a number")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("Discount percentage must be a number")
    if original_price < 0:
        raise ValueError("Original price cannot be negative")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = original_price * (discount_percentage / 100.0)
    final_price = original_price - discount_amount
    return final_price

if __name__ == '__main__':
    sample_original = 199.99
    sample_discount = 20
    result = calculate_final_price(sample_original, sample_discount)
    print(result)